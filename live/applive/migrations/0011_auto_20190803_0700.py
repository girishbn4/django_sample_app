# Generated by Django 2.2.2 on 2019-08-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applive', '0010_auto_20190803_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='status',
            field=models.CharField(choices=[(None, 'Please select below option'), ('1', 'Active'), ('2', 'inactive'), ('3', 'pending')], max_length=100),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=100, verbose_name='lanuage name it is'),
        ),
    ]