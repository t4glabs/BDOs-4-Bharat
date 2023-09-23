# Copyright (c) 2023, T4GLabs and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from  frappe import get_doc

class WorkRequest(WebsiteGenerator):
	
	def on_update(self):
		pass

	def validate(self):
		# web view route
		if not self.route:
			self.route = f"{self.name}"

	def get_context(self, context):
		# context.theme_url = "sss"
		context.j_theme = frappe.db.get_value('Job Theme', self.job_theme , 'job_theme')
		context.collab = frappe.db.get_value('Collaboration', self.collaboration, 
		'collaboration')
		context.sw = frappe.db.get_value('Social Worker', self.social, 'name1')
		context.no_cache = 1
		return context

@frappe.whitelist(allow_guest=True)
def insert_doc(bdo, sw, theme):
	params = theme.split('-')
	req = get_doc({
		'doctype': 'Work Request',
		'block_official': bdo,
		'job_theme': params[0],
		'collaboration': params[1],
		'social': sw,
		'status': 'Open'
		})
	req.save(ignore_permissions=True)
	frappe.db.commit()
