# Generated by Django 3.2.4 on 2022-04-06 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0006_remove_associateddomain_association_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associateddomain',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='associateddomain',
            name='registrar',
        ),
    ]
