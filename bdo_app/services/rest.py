import frappe
from frappe import get_doc

@frappe.whitelist(allow_guest=True)
def workRequest(bdo, sw):
    theme = frappe.form_dict["theme"]
    print(f'\n\n\n {bdo}\n{sw}\n {theme} \n\n\n')





    
         