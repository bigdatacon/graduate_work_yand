# Generated by Django 4.1 on 2022-10-17 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_question_file_path'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='filefilmwork',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='filefilmwork',
            name='file',
        ),
        migrations.RemoveField(
            model_name='filefilmwork',
            name='film_work',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='FileFilmWork',
        ),
    ]
