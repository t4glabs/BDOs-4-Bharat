# Copyright (c) 2023, T4GLabs and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class WorkRequest(WebsiteGenerator):
	
	def on_update(self):
		pass

	def validate(self):
		# web view route
		if not self.route:
			self.route = f"{self.name}"

	def get_context(self, context):
		context.theme = frappe.db.get_value('Job Theme', self.job_theme , 'job_theme')
		context.collab = frappe.db.get_value('Collaboration', self.collaboration, 'collaboration')
		context.no_cache = 1

		return context

@frappe.whitelist(allow_guest=True)
def insert_doc(bdo, sw, theme):
    
    print(f'\n\n\n hrloo {bdo}\n{sw}\n {theme}  \n\n\n')
