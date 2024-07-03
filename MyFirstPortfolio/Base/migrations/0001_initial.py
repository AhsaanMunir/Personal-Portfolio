# Generated by Django 5.0.6 on 2024-06-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=40)),
                ("content", models.TextField(max_length=400)),
                ("number", models.CharField(max_length=10)),
            ],
        ),
    ]
