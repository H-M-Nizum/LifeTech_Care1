# Generated by Django 5.0 on 2024-01-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patientmodel_age_patientmodel_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmodel',
            name='age',
            field=models.IntegerField(),
        ),
    ]
