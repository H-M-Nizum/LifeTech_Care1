# Generated by Django 5.0 on 2024-01-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctormodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctormodel',
            name='qualification',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctormodel',
            name='meet_link',
            field=models.CharField(default='', max_length=200),
        ),
    ]
