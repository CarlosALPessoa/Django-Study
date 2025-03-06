from django.urls import path # type: ignore

from .views import *

app_name = "home"

urlpatterns = [
    path('', home, name="main"),
]