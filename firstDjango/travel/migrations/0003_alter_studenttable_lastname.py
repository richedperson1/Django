# Generated by Django 4.2.2 on 2023-07-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_studenttable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttable',
            name='lastName',
            field=models.CharField(max_length=22),
        ),
    ]
