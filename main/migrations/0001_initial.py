# Generated by Django 3.2 on 2021-05-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(max_length=400, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
