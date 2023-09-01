import frappe
from frappe import get_doc
import random


def on_user_signup(doc, method):
    user = doc.email

    user_doc = get_doc('User', {'email': user})
    user_doc.append('roles', {
        'role': 'Social Worker'
    })
    user_doc.save(ignore_permissions=True)

    permission = get_doc({
        "doctype": "User Permission",
        "user": user,
        "allow": 'Social Worker',
        "for_value": user
    })
    permission.save(ignore_permissions=True)
    frappe.db.commit()

