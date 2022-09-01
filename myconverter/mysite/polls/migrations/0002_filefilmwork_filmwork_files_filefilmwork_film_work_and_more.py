# Generated by Django 4.1 on 2022-09-01 17:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileFilmWork",
            fields=[
                (
                    "created",
                    models.DateTimeField(
                        auto_created=True, auto_now_add=True, verbose_name="Created"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="id",
                    ),
                ),
                (
                    "file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.fileupl"
                    ),
                ),
            ],
            options={
                "verbose_name": "FileFilmWork",
                "verbose_name_plural": "FileFilmWork",
            },
        ),
        migrations.AddField(
            model_name="filmwork",
            name="files",
            field=models.ManyToManyField(
                related_name="filmworks",
                through="polls.FileFilmWork",
                to="polls.fileupl",
            ),
        ),
        migrations.AddField(
            model_name="filefilmwork",
            name="film_work",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="polls.filmwork"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="filefilmwork",
            unique_together={("film_work", "file")},
        ),
    ]
