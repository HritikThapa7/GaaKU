# Generated by Django 3.1 on 2020-08-24 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('Account', '0003_auto_20200824_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='productname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
