# Generated by Django 2.1.7 on 2019-04-02 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appartement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='structureappartement',
            old_name='composant',
            new_name='composantAppartement',
        ),
    ]
