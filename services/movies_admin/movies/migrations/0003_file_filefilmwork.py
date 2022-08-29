# Generated by Django 3.2.7 on 2022-04-03 05:10

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210919_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('file_path', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='File')),
                ('file_format', models.CharField(max_length=100, verbose_name='File format')),
                ('video_codec', models.CharField(max_length=100, verbose_name='Video codec')),
                ('video_width', models.IntegerField(verbose_name='Width')),
                ('video_height', models.IntegerField(verbose_name='Height')),
                ('video_fps', models.IntegerField(verbose_name='Video FPS')),
                ('audio_codec', models.CharField(max_length=100, verbose_name='Audio codec')),
                ('audio_sample_rate', models.IntegerField(verbose_name='Audio sample rate')),
                ('audio_channels', models.IntegerField(verbose_name='Audio channels')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'db_table': '"content"."file"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FileFilmWork',
            fields=[
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Created')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'db_table': '"content"."file_film_work"',
                'managed': False,
            },
        ),
    ]
