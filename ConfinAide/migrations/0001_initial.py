# Generated by Django 3.0.6 on 2020-05-22 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=20, null=True)),
                ('prenom', models.CharField(max_length=20, null=True)),
                ('tel', models.CharField(max_length=20, null=True)),
                ('adresse', models.CharField(max_length=20, null=True)),
                ('nbr_personne', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name_Pretty', models.CharField(max_length=50)),
                ('prix', models.FloatField()),
                ('desc', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DicoProduce',
            fields=[
                ('id_dico', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('id_produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfinAide.Produit')),
            ],
        ),
        migrations.CreateModel(
            name='commande_produit',
            fields=[
                ('id_commande_produit', models.AutoField(primary_key=True, serialize=False)),
                ('confirm', models.CharField(choices=[('w', 'En attente'), ('v', 'Validée'), ('r', 'Rejetée')], default='En attente', max_length=30)),
                ('description', models.CharField(max_length=20)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfinAide.Client')),
                ('name_produit', models.ManyToManyField(to='ConfinAide.DicoProduce')),
            ],
        ),
    ]
