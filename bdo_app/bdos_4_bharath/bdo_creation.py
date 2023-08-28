import frappe
from frappe import get_doc
import random

def on_user_signup(doc, method):
    user = doc.email

    user_doc = get_doc('User', {'email': user})
    user_doc.append('roles', {
        'role': 'Block Official'
    })
    user_doc.save(ignore_permissions=True)
    frappe.db.commit()

    # if not frappe.db.exists("Block Official", {"email": user}):
        # bdo = get_doc({
        #     "doctype": "Block Official",
        #     "email": user
        # })
        # bdo.save(ignore_permissions=True)
        # assign learner role
        


# user = doc.email

#     if not frappe.db.exists({"doctype":"Block Offcial","user": user}):
#         bdo = get_doc({
#             "doctype": "Block Official",
#             "mail": user
#         })
#         bdo.save(ignore_permissions=True)
#         user_doc = get_doc('User', {'email': user})
#         user_doc.append('roles', {
#             'role': 'Block Official'
#         })
#         user_doc.save(ignore_permissions=True)
#         frappe.db.commit()
