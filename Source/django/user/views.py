from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "Oturum açıldı.")
            messages.add_message(request, messages.INFO, username + ", Hoşgeldiniz.")

            return redirect("index")
        else:
            messages.add_message(
                request, messages.ERROR, "Kullanıcı adı veya Parola yanlış"
            )
    login_form = AuthenticationForm()

    context = {
        "login_form": login_form,
    }

    return render(
        request=request,
        template_name="user/login.html",
        context=context
    )


@login_required(login_url="/user/login/")
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, "Oturumunuz kapatıldı.")

    return redirect("index")
