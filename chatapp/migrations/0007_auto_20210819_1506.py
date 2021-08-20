# Generated by Django 3.2.6 on 2021-08-19 15:06

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_auto_20210819_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(default='', validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='message',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]