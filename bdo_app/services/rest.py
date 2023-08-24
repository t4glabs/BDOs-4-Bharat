import frappe
from frappe import get_doc

@frappe.whitelist(allow_guest=True)
def get_volunteers(theme,collaboration):

    social_workers = []
    docs = []
    tests = frappe.db.get_list(
			'Work Theme Test',
			filters = {
				'parent': ['!=', '']
			},
			fields = ['job_theme', 'parent']
    	)

    for test in tests:
        if test.job_theme == theme:
            social_workers.append(test.parent)
    print(f'\n\n\n parent: {social_workers} \n\n\n')

    if social_workers:
        docs = frappe.db.get_list(
			'Social Worker',
			filters = {
				'name': ['in', social_workers]
			},
			fields = ['name1', 'email']
    	)
    return docs






    
         