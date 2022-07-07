from django.contrib import admin
from .models import Avasus

class ListadeCursos(admin.ModelAdmin):
    list_display =('id', 'nome_curso', 'publicada')
    list_display_links = ('id', 'nome_curso')
    search_fields = ('nome_curso', )
    list_filter = ('ch', 'idade',)
    list_editable = ('publicada',)
    list_per_page = 5
admin.site.register(Avasus, ListadeCursos)
