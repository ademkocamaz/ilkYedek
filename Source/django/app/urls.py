from django.urls import path

from app import views

urlpatterns = [
    path(route="", view=views.index, name="index"),
]
