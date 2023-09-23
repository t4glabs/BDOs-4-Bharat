# Copyright (c) 2023, T4GLabs and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class SocialWorker(WebsiteGenerator):
	def on_update(self):
		pass		
		

		# print(f'\n\n\n volunteer:{workers} \n\n\n')
		# job_theme = 

		# collab = frappe.db.get_list(
		# 	'Collaboration',
		# 	fields=['name','collaboration']
    	# )
		# print(f'\n\n\n self: {collab} \n\n\n')

		# job_themes = []  # Initialize an empty array to store the values
		# print(f'\n\n\n self: {self.job_theme} \n\n\n')
		
		# social_workers = frappe.db.get_list(
		# 	'Social Worker',
		# 	fields=['job_theme']
    	# )

		# tests = frappe.db.get_list(
		# 	'Work Theme Test',
		# 	filters = {
		# 		'parent': ['!=', '']
		# 	},
		# 	fields = ['job_theme', 'parent']
    	# )

		# for test in tests:
		# 	job_themes.append(test.job_theme)

		# print(f'\n\n\n tests: {test} \n\n\n')
		# print(f'\n\n\n themes: {job_themes} \n\n\n')



		# print(f'\n\n\n docs: {social_workers} \n\n\n')
		

		# for obj in social_workers:
		# 	job_themes.append(obj.job_theme)

		# 

	# 	filters={
		# 		'job_theme': 'housing'
		# 	},
		# 	fields = ['name1']

