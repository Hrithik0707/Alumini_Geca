# Generated by Django 2.2.6 on 2020-03-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumini', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='img',
            field=models.ImageField(default=None, upload_to='mydocs'),
        ),
    ]