# Generated by Django 4.2.2 on 2023-07-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutPage', '0008_studenttable_age1'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttable',
            name='age',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]