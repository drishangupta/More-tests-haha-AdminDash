# Generated by Django 5.0.7 on 2024-07-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Page', '0002_remove_datas_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='datas',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Level'),
            preserve_default=False,
        ),
    ]