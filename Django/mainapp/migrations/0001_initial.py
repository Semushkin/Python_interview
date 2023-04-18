# Generated by Django 4.2 on 2023-04-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('data_received', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('unit', models.IntegerField()),
                ('supplier', models.CharField(max_length=64)),
            ],
        ),
    ]
