import frappe
import datetime
from datetime import datetime

def get_context(context):

    user_roles = frappe.get_roles()
    if 'Block Official' in user_roles:
        reqs = frappe.db.get_list('Work Request',
                                    filters={
                                        'block_official': frappe.session.user
                                    },
                                    fields=['name', 'creation'])
    
    if 'Social Worker' in user_roles:
        reqs = frappe.db.get_list('Work Request',
                                    filters={
                                        'social': frappe.session.user
                                    },
                                    fields=['name', 'creation'])
    # date = reqs.creation.split(' ')[0]
    # print(f'\n\n\n {reqs} \n\n\n')
    context.reqs = reqs
    context.show_sidebar = 1
    context.no_cache = 1
    return context

