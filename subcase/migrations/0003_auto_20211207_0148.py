# Generated by Django 3.2.9 on 2021-12-06 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcase', '0002_transactions_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='organization_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subcase.organizations'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_status',
            field=models.CharField(default='Waiting..', max_length=200),
        ),
    ]
