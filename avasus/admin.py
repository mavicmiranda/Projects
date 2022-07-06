from django.contrib import admin
from .models import Avasus

class ListadeCursos(admin.ModelAdmin):
    list_display =('id', 'nome_curso')
    list_display_links = ('id', 'nome_curso')
    search_fields = ('nome_curso', )
    list_filter = ('ch', 'idade',)
    list_per_page = 3
admin.site.register(Avasus, ListadeCursos)
