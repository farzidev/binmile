# Generated by Django 3.0.3 on 2020-04-04 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_auto_20200404_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobprofile',
            name='curriculum_vitaes',
        ),
        migrations.DeleteModel(
            name='CVFile',
        ),
    ]
