from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
import urbackup_api
from datetime import datetime

@login_required(login_url="/user/login/")
def index(request):
    server = urbackup_api.urbackup_server("http://192.168.10.10:55414/x", "ilkadam", "764864")
    clients=server.get_status()
    for client in clients:
        messages.add_message(request, messages.INFO, datetime.fromtimestamp(client["lastbackup"]).strftime("%x %X"))

    return render(request=request, template_name="app/index.html")
