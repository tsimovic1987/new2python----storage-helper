# Generated by Django 5.1.1 on 2024-09-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('number', models.TextField(blank=True, null=True)),
                ('beschreibung', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
