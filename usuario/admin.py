from django.contrib import admin

from .models import Usuario

class ListaUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email','CPF')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 2

admin.site.register(Usuario, ListaUsuarios)

