
from ConfinAide.models import Client, commande_produit, Produit, DicoProduce

def Validation(request):
    mail = request.session.get("id_mail",None)
    password = request.session.get("id_password",None)
    if(mail==None or password==None): return False
    
    client = Client.objects.get(mail=mail,password=password)
    produits = [o.name for o in Produit.objects.all()]
    
    commande = commande_produit(id_client = client)
    commande.save()

    for p in produits:
        produit = Produit.objects.get(name=p)
        q = request.session.get(p,0)

        dicoProd = DicoProduce(id_produce=produit, quantity=q)
        dicoProd.save()

        commande.name_produit.add(dicoProd)

        request.session[p] = 0
    return True
            
            