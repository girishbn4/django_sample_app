# Generated by Django 2.2.2 on 2019-08-03 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applive', '0009_auto_20190803_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'inactive'), ('3', 'pending'), (None, 'Please select below option')], max_length=100),
        ),
    ]
