# Generated by Django 3.0.3 on 2020-04-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_auto_20200404_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='order',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=2, null=True),
        ),
    ]