let valid  =true

let csrftoken = getCookies("csrftoken")
const authUser = (username, password) =>{
    $.ajax({
        url:"/login/user/",
        method:"POST",
        data:{
            "username":username,
            "password" : password,
            csrfmiddlewaretoken: csrftoken
        },
        success:(res)=>{
            console.log(res)
            if (res["status"]){
              window.location.href = "/home/"
            }
            else {
                document.querySelector("#loginErr").classList.remove("hidden")
            }
        }   

    })
}

document.getElementById("loginForm")
.addEventListener("submit",(e) =>{
    e.preventDefault()
    document.querySelectorAll(".required").forEach(elem =>{
        if(elem.value.length <=0){
            valid = false
            elem.style.borderColor = "#dc3545"
        }
        else{
            valid = true
            elem.style.borderColor ="royalblue"
        }
    })
    if(valid){
        authUser(e.target.username.value, e.target.password.value)
    }
})