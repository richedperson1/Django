# Generated by Django 4.2.2 on 2023-07-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('mobNumber', models.IntegerField()),
                ('emailID', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
