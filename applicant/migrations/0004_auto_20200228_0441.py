# Generated by Django 3.0.3 on 2020-02-28 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_remove_personal_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='internationalqualifications',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='nextofkin',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='southafricanqualifications',
            name='applicant',
        ),
    ]