# Generated by Django 3.2.12 on 2022-03-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftManagementApp', '0006_auto_20220303_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shop_id',
            field=models.IntegerField(default=1, verbose_name='shop_id'),
            preserve_default=False,
        ),
    ]
