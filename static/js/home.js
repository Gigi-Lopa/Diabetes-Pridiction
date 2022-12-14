let csrfToken = getCookies("csrftoken")
let valid = true
let isNum;

const placeResults = (res) =>{
    let showResults =  document.querySelector(".show-results")
    let reportTable = document.querySelector(".report-table") 
    let PREDICTION_REPORT = ["precision", "recall", "f1-score", "support"]
    
    let noDiabeto = ` <b><span class="bi bi-hand-thumbs-up-fill"></span> Congratulations </b> Diabetes was <b>NOT</b> detected in you system.
    For insurance eat health and visit <a href="https://diabetesjournals.org/">Diabetes Warriors</a> for more tips.`

    let yesDiabeto = ` <b><span class="bi bi-exclamation-triangle-fill"></span> Unfortunatly, </b> Diabetes <b>WAS</b> detected in you system.
    Eat health, exercise regulary and visit <a href="https://diabetesjournals.org/">Diabetes Warriors</a> for more health tips.`
    
    document.querySelector(".results-message").innerHTML = ""
    showResults.classList.remove("hidden")
    reportTable.classList.remove("hidden")

    if (res["healthStatus"] == "0"){
        showResults.classList.add("no-diabetes")
        $(".results-message").append(noDiabeto)
    }
    else if (res["healthStatus"] == "1"){

        showResults.classList.add("yes-diabetes")

        $(".results-message").append(yesDiabeto)

    }

    for (let i =0; i < PREDICTION_REPORT.length; i++){
        reportTable.querySelector("#"+PREDICTION_REPORT[i]).innerHTML = Math.floor(res["report"][PREDICTION_REPORT[i]]*100) + "% "
    }
    reportTable.querySelector("#support").innerHTML = ""
    reportTable.querySelector("#support").innerHTML = res["report"]["support"]

}
let addTableRow = (data, prediction)=>{
    let HISTORY = document.querySelector("#userHistory")
    let tableRows = ["preganancies", "glucose", "bp", "insulin", "BMI", "DiabetesPedigreeFunction", "age" ]
    let tr = document.createElement("tr")
    for (let i = 0; i < tableRows.length; i++){
        let td = document.createElement("td")
        td.innerHTML = data[tableRows[i]]
        tr.appendChild(td)
    }
    let td = document.createElement("td")
    td.innerHTML = (prediction == 1) ? ("Diabetic") : ("Not Diabetic")
    tr.appendChild(td)   
    HISTORY.appendChild(tr)
}
const fetchHealthStatus = (data) =>{
    $.ajax({
        url:"/check/status/",
        type:"POST",
        data:{
            data,
            csrfmiddlewaretoken: csrfToken
        },
        success:(res)=>{
            placeResults(res)
            addTableRow(data, res["healthStatus"])
        }
    }) 
}
document.querySelector("#predictionForm")
.addEventListener("submit", (e)=>{
    e.preventDefault()
    let DPF
    document.querySelectorAll(".required").forEach(input =>{
          
        if (input.value.length == 0){
            valid = false
            input.style.borderColor = "red"
        }
        else{
            valid = true
            input.style.borderColor = "royalblue"
        }
      
    })
    document.querySelectorAll("input[type='text']").forEach(inputText =>{
        isNum = parseFloat(inputText.value)

        if(isNaN(isNum)){
            valid = false
            inputText.style.borderColor = "red"
        }
        else{
            valid = true
            inputText.style.borderColor = "royalblue"
        }
    })
    document.querySelectorAll(".pdf").forEach((radio) =>{
            if (radio.checked === true && radio.value === "yes"){
                DPF = 1
            }
            else if (radio.checked === true && radio.value === "no"){
                DPF = 0
            }
    })
    
    if (valid){
        fetchHealthStatus({
            "preganancies": e.target.preganancies.value,
            "glucose": e.target.glucose.value,
            "bp": e.target.BP.value,
            "insulin": e.target.insulin.value,
            "BMI": e.target.BMI.value,
            "DiabetesPedigreeFunction": DPF,
            "age": e.target.age.value
        })
        }
    
})
