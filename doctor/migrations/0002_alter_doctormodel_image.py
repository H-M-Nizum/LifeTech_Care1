# Generated by Django 5.0 on 2024-01-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor/images/'),
        ),
    ]