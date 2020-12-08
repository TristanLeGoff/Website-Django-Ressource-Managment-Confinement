from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import ConfinAide.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('commandes/', views.commandes, name='commandes'),
    path('panier/',views.panier, name='panier'),
    path('delPanier/', views.delPanier, name='delPanier'),
    path('commandes_specifique/', views.commandes_specifique, name='commandes_specifique'),
    path('statistique/', views.statistique, name='statistique')
]

urlpatterns += staticfiles_urlpatterns()