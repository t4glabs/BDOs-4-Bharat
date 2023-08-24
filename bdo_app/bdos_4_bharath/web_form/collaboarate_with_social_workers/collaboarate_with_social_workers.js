frappe.ready(function() {
	let btn = document.querySelector('.submit-btn')
	btn.addEventListener('click', redirect)

	function redirect(){
		let job_theme = frappe.web_form.get_value('job_theme')
		let collaboration = frappe.web_form.get_value('collaboration')
		window.alert(job_theme, collaboration);
		window.location.href = "http://b-4-b.com:8002/"
	}
})