# Generated by Django 3.0.7 on 2020-11-07 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0010_enginetype_vulnerability_scan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enginetype',
            name='subdomain_takeover',
        ),
    ]
