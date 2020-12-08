from django.contrib import admin
from .models import *

def make_validate(modeladmin, request, queryset):
    queryset.update(confirm='v')
make_validate.short_description = "Valider les commandes selectionnées"

def make_false(modeladmin, request, queryset):
    queryset.update(confirm='r')
make_false.short_description = "Rejeter les commandes selectionnées"

class PannierAdmin(admin.ModelAdmin):
    list_display = ('id_commande_produit', 'id_client', 'confirm')
    actions = [make_validate,make_false]



admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(DicoProduce)
admin.site.register(commande_produit,PannierAdmin)
