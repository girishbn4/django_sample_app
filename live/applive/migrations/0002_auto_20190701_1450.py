# Generated by Django 2.2.2 on 2019-07-01 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='channels',
            name='channel_path',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='channels',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applive.Country', verbose_name='country_id'),
        ),
        migrations.AlterField(
            model_name='channels',
            name='language_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applive.Language', verbose_name='language_id'),
        ),
        migrations.AlterField(
            model_name='language',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applive.Country', verbose_name='country_id'),
        ),
        migrations.AddField(
            model_name='channels',
            name='attachments',
            field=models.ManyToManyField(to='applive.Media'),
        ),
        migrations.AddField(
            model_name='country',
            name='attachments',
            field=models.ManyToManyField(to='applive.Media'),
        ),
        migrations.AddField(
            model_name='language',
            name='attachments',
            field=models.ManyToManyField(to='applive.Media'),
        ),
    ]
