# Generated by Django 3.2.8 on 2021-10-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20211018_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moringamerch',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
