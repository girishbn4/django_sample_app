# Generated by Django 2.2.2 on 2019-07-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applive', '0006_auto_20190725_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channels',
            name='logo',
            field=models.ImageField(upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='country',
            name='logo',
            field=models.ImageField(upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='language',
            name='logo',
            field=models.ImageField(upload_to='logo'),
        ),
    ]
