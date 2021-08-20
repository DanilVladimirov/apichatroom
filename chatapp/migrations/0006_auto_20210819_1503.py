# Generated by Django 3.2.6 on 2021-08-19 15:03

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_auto_20210819_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 15, 3, 38, 829643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(default='', validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='message',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 15, 3, 38, 829714, tzinfo=utc)),
        ),
    ]