# Generated by Django 4.2 on 2023-04-18 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='unit',
            new_name='quantity',
        ),
    ]
