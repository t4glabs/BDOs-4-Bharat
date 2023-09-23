frappe.ready(()=>{

    let a = document.querySelector('.submit-btn')

    document.querySelector(".request_info").addEventListener("submit", displayVolunteers)
    function displayVolunteers(e){

        e.preventDefault();

        let details = [
            document.querySelector('#job-theme').value,
            document.querySelector('#collaborations').value
        ]

        let url = window.location.href,
            base_url = url.split('?')[0],
            redirect = `${base_url}?collab=${details[0]}-${details[1]}`
        
        window.location.href = redirect
        
    }

    const notifyButtons = document.querySelectorAll('.notify-btn');

    notifyButtons.forEach(btn=>{
        btn.addEventListener('click', ()=>{
            
            let sw = btn.getAttribute('data-parent')

            const queryParams = new URLSearchParams(window.location.search);

            // Get the value of the 'theme' parameter
            const themeValue = queryParams.get('collab');


            frappe.call({
                // method: "bdo_app.services.rest.workRequest",
                method: "bdo_app.bdos_4_bharath.doctype.work_request.work_request.insert_doc",
                args: {
                    bdo: frappe.session.user,
                    sw: sw,
                    collab: themeValue
                },
                callback: (data) => {
                        console.log('done')
            
                    frappe.show_alert({
                        message: __("Collaboration Request Send"),
                        indicator: "green",
                    });
                    setTimeout(() => {
                        let url = window.location.href,
                            base_url = url.split('?')[0] 
                    
                        window.location.href = base_url
                    }, 3000);
                },
            });
            
            })
   

    })
    

})

// 'bdo_app.www.index.get_volunteers'
// 'bdo_app.services.rest.get_volunteers'




// First 

// function displayVolunteers(e){
//     e.preventDefault();
//     console.log("displayVolunteers")
//     let details = [
//         cdocument.querySelector('#job-theme').value,
//         document.querySelector('#collaborations').value
//     ]

    
//     frappe.call({
//         // method: 'bdo_app.www.request-help.get_volunteers',
//         method: 'bdo_app.services.rest.get_volunteers',
//         args: {
//             'theme': details[0],
//             'collaboration': details[1]
//         },
//         callback: r => {
//             console.log(r.message)
//             // console.log($("#reloadContent"))
//             // frappe.provide('result');
//             // result = r.message;

//         }
//     })
// }