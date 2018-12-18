# Generated by Django 2.1.4 on 2018-12-18 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codebanque', models.CharField(max_length=25, unique=True)),
                ('libbanque', models.CharField(max_length=100)),
                ('pays', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='countries_plus.Country')),
            ],
        ),
    ]
