# Generated by Django 4.1 on 2022-08-31 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_file_filefilmwork_filmwork"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fileupl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filename", models.CharField(max_length=200)),
                (
                    "file_path",
                    models.FileField(upload_to="files/", verbose_name="File"),
                ),
            ],
        ),
    ]
