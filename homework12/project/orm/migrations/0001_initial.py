# Generated by Django 3.2.6 on 2021-08-17 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Homework",
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
                ("task", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="HomeworkResult",
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
                ("solution", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orm.student"
                    ),
                ),
                (
                    "homework",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orm.homework"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="homework",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orm.teacher"
            ),
        ),
    ]
