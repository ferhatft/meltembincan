# Generated by Django 4.1.7 on 2023-04-26 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0016_delete_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='btntitle',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='link',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='subtitle',
        ),
    ]
