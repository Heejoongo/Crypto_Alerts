# Generated by Django 3.2.23 on 2023-11-03 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='base_currency',
            field=models.CharField(choices=[('BTC', 'BTC'), ('ETH', 'ETH'), ('USD', 'USD'), ('EUR', 'EUR')], default='BTC', max_length=10),
        ),
        migrations.AddField(
            model_name='alert',
            name='quote_currency',
            field=models.CharField(choices=[('BTC', 'BTC'), ('ETH', 'ETH'), ('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=10),
        ),
        migrations.AddField(
            model_name='alert',
            name='threshold_value',
            field=models.DecimalField(decimal_places=8, default=5000, max_digits=20),
        ),
        migrations.AddField(
            model_name='alert',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL),
        ),
    ]