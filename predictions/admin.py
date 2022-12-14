from django.contrib import admin
from predictions.models import usersModel, userHistory

# Register your models here.
admin.site.register(usersModel)
admin.site.register(userHistory)