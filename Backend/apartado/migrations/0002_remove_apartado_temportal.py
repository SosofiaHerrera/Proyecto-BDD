# Generated by Django 5.0.4 on 2024-05-13 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartado',
            name='temportal',
        ),
    ]
