# Generated by Django 2.1.4 on 2019-08-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_auto_20190809_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
