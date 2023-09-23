import frappe
from frappe import get_doc
from frappe import _

docs = []
params = []
default = ['', '']

def get_context(context):

    context.no_result = False
    if frappe.form_dict:       
        j_theme = frappe.form_dict["collab"]
        params = j_theme.split('-')
        try:          
           result = get_volunteers(params[0], params[1])
           context.result = result
           if len(result) == 0:
               context.no_result = True
               
        except Exception as e:
            frappe.throw(('An error occurred while fetching volunteer details'))

    # get themes and collaboration lists
    context.collabs = frappe.db.get_list(
			'Collaboration',
			fields=['name','collaboration']
    	)
    context.themes = frappe.db.get_list(
			'Job Theme',
			fields=['name','job_theme']
    	)

    context.show_sidebar = 1
    context.no_cache = 1
    
    return context



@frappe.whitelist(allow_guest=True)
def get_volunteers(j_theme, collaboration):
    docs= []
    social_workers = frappe.db.sql_list(
        """
        SELECT DISTINCT t1.parent
        FROM `tabWork Theme Test` t1
        JOIN `tabSelect Collaboration` t2 ON t1.parent = t2.parent
        WHERE t1.parent IS NOT NULL
        AND t1.job_theme = %s
        AND t2.collaboration = %s
        """,
        (j_theme, collaboration)
    )
    

    # place of bdo
    district = frappe.db.get_value('Block Official', frappe.session.user, 'district')

    if social_workers:
        docs = frappe.db.get_list(
			'Social Worker',
			filters = {
				'name': ['in', social_workers],
                # 'district': district
			},
			fields = ['name','name1', 'email', 'photo', 'years_of_experience', 'show_contact']
    	)

    return docs



# before
# @frappe.whitelist(allow_guest=True)
# def get_volunteers(theme,collaboration):
#     docs = []
#     tests = frappe.db.get_list(
#         'Work Theme Test',
        
#         filters = {
#             'parent': ['!=', ''],
#             'job_theme': theme
#         },
#         fields = ['parent']
#     )
	
#     themes = []
#     for test in tests:
#         themes.append(test['parent'])

#     collabs = frappe.db.get_list(
#         'Select Collaboration',
#         filters = {
#             'parent': ['!=', ''],
#             'collaboration': collaboration
#         },
#         fields = ['parent']
#     )
#     help = []
#     for test in collabs:
#         help.append(test['parent'])

#     social_workers = [parent for parent in help if parent in themes]

#     # place of bdo
#     district = frappe.db.get_value('Block Official', frappe.session.user, 'district')

#     if social_workers:
#         docs = frappe.db.get_list(
# 			'Social Worker',
# 			filters = {
# 				'name': ['in', social_workers]
#                 # 'district': district
# 			},
# 			fields = ['name1', 'email', 'photo', 'years_of_experience', 'show_contact']
#     	)
        
#     return docs



