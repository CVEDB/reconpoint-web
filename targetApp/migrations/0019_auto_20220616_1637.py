# Generated by Django 3.2.4 on 2022-06-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0018_domaininfo_name_servers'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
