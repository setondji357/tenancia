# Generated by Django 2.1.4 on 2018-12-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=132)),
                ('prenom', models.CharField(max_length=132)),
                ('addresse', models.CharField(max_length=32)),
            ],
        ),
    ]
