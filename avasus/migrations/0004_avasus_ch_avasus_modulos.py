# Generated by Django 4.0.5 on 2022-07-05 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avasus', '0003_remove_avasus_ch'),
    ]

    operations = [
        migrations.AddField(
            model_name='avasus',
            name='ch',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='avasus',
            name='modulos',
            field=models.IntegerField(null=True),
        ),
    ]