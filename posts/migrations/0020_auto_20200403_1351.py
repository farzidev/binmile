# Generated by Django 3.0.3 on 2020-04-03 13:51

from django.db import migrations, models
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20200403_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microsoftdynamics365',
            name='order',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=2, null=True, validators=[posts.validators.md_order_validator]),
        ),
    ]