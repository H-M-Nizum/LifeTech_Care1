# Generated by Django 5.0 on 2024-02-16 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_remove_buymedicinemodel_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buymedicinemodel',
            name='medicine',
        ),
    ]
