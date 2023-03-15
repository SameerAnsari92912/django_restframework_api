var loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"

if (loginform){
    //handle this login form 
    loginForm.addEventListener('submit',handleLogin)

    }


function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndpoint = '${baseEndpoint}/token/'
    let loginFormData = new FormData(loginForm)
    const options = {
        method:"POST",
        headers:{
            "ContentType":"application/json"
        },
        body:""
    }
    fetch(loginEndpoint,options)
}