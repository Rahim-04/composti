# Generated by Django 4.1.7 on 2023-04-11 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0009_composteur_desponible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composteur',
            name='image',
            field=models.ImageField(blank=True, default='profil.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='greener',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]