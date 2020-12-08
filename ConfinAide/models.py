from django.db import models

class Client(models.Model):
    id_client = models.AutoField(primary_key=True, )
    password = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 50)
    nom = models.CharField(max_length = 20, null = True)
    prenom = models.CharField(max_length = 20, null=True)
    tel = models.CharField(max_length = 20, null = True)
    adresse = models.CharField(max_length = 20, null = True)
    nbr_personne = models.CharField(max_length=2, null=True)
    
    def __str__(self):
        return self.adresse
    
class Produit(models.Model):
    name = models.CharField(primary_key = True, max_length = 20)
    name_Pretty = models.CharField(max_length = 50)
    prix = models.FloatField()
    desc = models.CharField(max_length = 250)
    def __str__(self):
        return self.name_Pretty

class DicoProduce(models.Model):
    id_dico = models.AutoField(primary_key = True)
    id_produce = models.ForeignKey(Produit, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return str(str(self.id_produce)+" x"+str(self.quantity))

STATUS_CHOICES = [
    ('w', 'En attente'),
    ('v', 'Validée'),
    ('r', 'Rejetée'),
]

class commande_produit(models.Model):
    id_commande_produit = models.AutoField(primary_key = True)
    name_produit = models.ManyToManyField(DicoProduce)
    id_client = models.ForeignKey(Client, on_delete = models.CASCADE)
    confirm = models.CharField(default = "En attente",max_length=30, choices=STATUS_CHOICES)
    description = models.CharField(max_length = 20)