# Generated by Django 2.2.6 on 2020-03-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumini', '0002_events_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]