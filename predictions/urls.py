from django.urls import path
from . import views as vs

urlpatterns = [
    path("", vs.render_login),
    path("home/", vs.render_home),
    path("create/account/", vs.render_create_acc),
    path("login/user/", vs.authLogin),
    path("create/user/acc", vs.create_acc),
    path("check/status/", vs.predict),
]