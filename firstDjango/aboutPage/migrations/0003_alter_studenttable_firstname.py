# Generated by Django 4.2.2 on 2023-07-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutPage', '0002_alter_studenttable_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttable',
            name='firstName',
            field=models.CharField(max_length=23),
        ),
    ]
