from django.contrib import admin

# Register your models here.
from app.models import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Server._meta.fields]
    list_display_links = [field.name for field in Server._meta.fields]
