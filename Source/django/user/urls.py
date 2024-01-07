from django.urls import path
from user import views

urlpatterns = [
    path(route="login/", view=views.login, name="login"),
    path(route="logout/", view=views.logout, name="logout"),
]
