# Generated by Django 4.2.2 on 2023-07-20 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutPage', '0006_alter_studenttable_emailid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenttable',
            name='age',
        ),
    ]
