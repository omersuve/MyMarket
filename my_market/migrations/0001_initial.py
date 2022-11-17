# Generated by Django 4.1.3 on 2022-11-17 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Store",
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
                ("name", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=50, null=True)),
                ("description", models.TextField(null=True)),
                ("slug", models.SlugField(blank=True)),
                ("profiles", models.ManyToManyField(to="account.profile")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=50, null=True)),
                ("price", models.IntegerField(null=True)),
                ("slug", models.SlugField(blank=True)),
                ("profiles", models.ManyToManyField(to="account.profile")),
                (
                    "stores",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_market.store",
                    ),
                ),
            ],
        ),
    ]
