
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pythonCode import panier as pan, forms, commande
from .models import Produit, Client, commande_produit, DicoProduce

def index(request):
    return HttpResponseRedirect('/ConfinAide/connexion')

def panier(request):
    if request.method == "POST":
        pan.Update(request)
        return HttpResponseRedirect(reverse('commandes'))
    if request.method == "GET":
        c = list()
        for p in [o.name for o in Produit.objects.all()]:
            prix =  Produit.objects.get(name=p).prix
            q = request.session.get(p,0)
            c.append({"nom": p , "q" : q, "prixU": prix , "prixT" : float(prix) * int(q)})
        return render(request, "panier.html", {"produits" : c})
        
def connexion(request):
    test = forms.Verification(request)
    if request.method == "POST":
        if test:
            return HttpResponseRedirect(reverse("commandes"))
        else:
            return HttpResponseRedirect(reverse("connexion"))
    if request.method == "GET":
        if test: return HttpResponseRedirect(reverse("commandes"))
        else: return render(request, "connexion.html")            
    
def inscription(request):
    if request.method == "POST":
        test = forms.Inscription(request)
        if(test):
            return HttpResponseRedirect(reverse("commandes"))
        else:
            return HttpResponseRedirect(reverse("inscription"))
    if request.method == "GET":
        return render(request, "inscription.html")

def deconnexion(request):
    if request.method == "GET":
        forms.Deconnexion(request)
        return HttpResponseRedirect(reverse("connexion"))

def commandes(request):
    if request.method == "GET":
        c = list()
        e = list()
        i = 0
        
        for p in [o.name for o in Produit.objects.all()]:
                if i == 3:
                    i = 0
                    c.append(e)
                    e = list()

                produit = Produit.objects.get(name=p)
                e.append({"name": p , "namePretty" : produit.name_Pretty, "prix": produit.prix , "desc" : produit.desc})
                i += 1
        if e not in c : c.append(e)
        return render(request, "listProduit.html", {"produits" : c})
    if request.method == "POST":
        if commande.Validation(request):
            return HttpResponseRedirect(reverse("panier"))
        else:
            return HttpResponse("Echec de la commande<br><a href='/ConfinAide/panier/'>Retour au panier</a>")

def delPanier(request):
    pan.Delete(request)
    return HttpResponseRedirect(reverse("panier"))

def statistique(request):
    if request.method == "GET":
        c1 = 0
        c2 = len(Client.objects.all())
        c3 = 0
        c4 = len(commande_produit.objects.all())
        
        for i in [o.nbr_personne for o in Client.objects.all()]:
            c1+=int(i)+1
        for cp in commande_produit.objects.all():
            for i in cp.name_produit.all():
                quant = i.quantity
                c3+=quant
        if (c4!=0):
            c3=c3/c4
        return render(request, "stats.html", {"NbrPersonnes": c1 , "NbrAdresses" : c2, "NbrProduits": c3 , "NbrLivraisons" : c4})

def commandes_specifique(request):
    return HttpResponse("Page en construction <a href='/ConfinAide/commandes/'>retour liste des produits</a>")
