# Generated by Django 3.0.5 on 2020-04-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0002_auto_20200425_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.FloatField(default=10, help_text='Transaction amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='shopper',
            field=models.CharField(default='eddy', help_text='User who initiated the transaction', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('CREATED', 'created'), ('SUCCESSFUL', 'successful'), ('FAILED', 'failed'), ('DISPUTED', 'disputed')], help_text='Payment status', max_length=20),
        ),
    ]