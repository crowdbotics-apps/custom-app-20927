# Generated by Django 2.2.16 on 2020-10-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("price", models.FloatField()),
                ("image", models.URLField()),
            ],
        ),
    ]
