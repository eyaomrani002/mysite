# Generated by Django 4.1.7 on 2023-03-07 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_categorie_produit_img_produit_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.TimeField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='Fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur'),
        ),
    ]
