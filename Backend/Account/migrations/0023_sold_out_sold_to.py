# Generated by Django 3.1 on 2020-09-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0022_remove_sold_out_sold_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold_out',
            name='sold_to',
            field=models.CharField(default='user', max_length=20),
        ),
    ]
