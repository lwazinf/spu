# Generated by Django 3.0.3 on 2020-02-28 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_auto_20200228_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='user',
        ),
    ]
