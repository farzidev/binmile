# Generated by Django 3.0.3 on 2020-04-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20200401_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='powerplatform',
            options={'ordering': ('-order',)},
        ),
        migrations.AlterModelOptions(
            name='servicenow',
            options={'verbose_name': 'ServiceNow', 'verbose_name_plural': 'ServiceNow'},
        ),
        migrations.AddField(
            model_name='powerplatform',
            name='order',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='highlight',
            field=models.TextField(help_text='Maximum characters allowed are 170', max_length=170),
        ),
        migrations.AlterField(
            model_name='servicenow',
            name='content',
            field=models.TextField(),
        ),
    ]
