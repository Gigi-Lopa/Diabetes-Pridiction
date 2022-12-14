from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from predictions.models import usersModel, userHistory
from predictions.utils import DiabetisPrediction

dp = DiabetisPrediction()
dp.createModel()

# Create your views here.

@csrf_exempt
def render_home(request):
    HISTORY = userHistory.objects.filter(userId =  request.session.get("id"))
    if request.session.get("username"):
        return render(request, "index.html", {
        "username": request.session.get("username"),
        "history": HISTORY
            })
    else:
        return HttpResponseRedirect("/")

@csrf_exempt
def render_login(request):
    return render(request, "login.html")

@csrf_exempt
def render_create_acc(request):
    return render(request, "createAccount.html")

@csrf_exempt
def authLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        logProps = usersModel.objects.filter(
            username = username,
            password = password
        )
        if logProps:
            request.session["username"] = username
            request.session["id"] = logProps[0].id
            return JsonResponse({
                "status": True,
                "username" : request.POST["username"]
            })
        else:
            return JsonResponse({
                "status": False,
            })

@csrf_exempt 
def create_acc(request):
    if request.method == "POST":
        userProps = usersModel(username = request.POST["username"],
        email = request.POST["email"],
        password = request.POST["password"]
    )        
        userProps.save()

        return HttpResponseRedirect("/")


@csrf_exempt
def predict(request):
    if request.method == "POST":
        prediction =dp.predict(request.POST, request.session.get("id")) 
        return JsonResponse({
            "healthStatus" : str(prediction[0]), 
            "report": prediction[1]
             })    


    