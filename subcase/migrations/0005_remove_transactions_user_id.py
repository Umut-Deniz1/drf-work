# Generated by Django 3.2.9 on 2021-12-06 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subcase', '0004_remove_transactions_organization_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='user_id',
        ),
    ]
