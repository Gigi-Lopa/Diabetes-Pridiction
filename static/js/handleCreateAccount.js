document.getElementById("createAccount")
.addEventListener("submit",(e) =>{
    document.querySelectorAll(".required").forEach(elem =>{
        if(elem.value.length <=0){
           e.preventDefault()
            elem.style.borderColor = "#dc3545"
        }
        else{
            elem.style.borderColor ="royalblue"
        }
    })
    if (e.target.username.value.length >= 15){
        e.preventDefault()
        document.querySelector("#username").style.borderColor = "red"
        document.getElementById("usernameErr").classList.remove("hidden")
    }
    if (e.target.password.value != e.target.confirmPassword.value){
        e.preventDefault()
        document.querySelector("#password").style.borderColor = "red"
        document.querySelector("#confirmPassword").style.borderColor = "red"
        document.getElementById("passwordError").classList.remove("hidden")
        
    }
})