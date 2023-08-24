frappe.ready(()=>{
    console.log('helloo')

    let a = document.querySelector('.submit-btn')
    // a.addEventListener('click', displayVolunteers)

    document.querySelector(".request_info").addEventListener("submit", displayVolunteers)
    
    function displayVolunteers(e){
        e.preventDefault();
        console.log("displayVolunteers")
        let details = [
            document.querySelector('#job-theme').value,
            document.querySelector('#collaborations').value
        ]

        let url = window.location.href,
            base_url = url.split('?')[0],
            redirect = `${base_url}?theme=${details[0]}-${details[1]}`
        
        console.log(redirect)
        
        window.location.href = redirect
        
    }
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