# Generated by Django 2.2.12 on 2022-07-31 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20220731_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
    ]