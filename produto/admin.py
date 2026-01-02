from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

class ProtudoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]

admin.site.register(Produto, ProtudoAdmin)
admin.site.register(Variacao)

