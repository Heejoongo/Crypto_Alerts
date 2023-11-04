# Generated by Django 3.2.23 on 2023-11-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_auto_20231103_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='last_checked',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alert',
            name='last_rate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
    ]