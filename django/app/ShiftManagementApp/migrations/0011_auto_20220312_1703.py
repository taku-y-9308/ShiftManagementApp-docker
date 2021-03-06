# Generated by Django 3.2.12 on 2022-03-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftManagementApp', '0010_user_default_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='position',
            field=models.BooleanField(default=True, verbose_name='position'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shift',
            name='begin',
            field=models.DateTimeField(verbose_name='begin'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='finish',
            field=models.DateTimeField(verbose_name='finish'),
        ),
    ]
