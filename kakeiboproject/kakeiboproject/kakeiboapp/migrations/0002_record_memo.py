# Generated by Django 3.2 on 2023-05-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeiboapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='memo',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]