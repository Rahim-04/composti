# Generated by Django 4.1.7 on 2023-04-27 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_transaction_delete_deshet_delete_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='grenneur',
            new_name='greeneur',
        ),
    ]