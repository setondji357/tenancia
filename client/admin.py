from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['nom', 'prenom', 'address']
    search_fields = 'id'


admin.register(Client, ClientAdmin)
