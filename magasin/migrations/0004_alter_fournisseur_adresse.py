# Generated by Django 4.1.7 on 2023-03-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fournisseur',
            name='adresse',
            field=models.TextField(),
        ),
    ]
