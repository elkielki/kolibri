# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-03-30 18:46
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("discovery", "0007_device_pinning"),
    ]

    operations = [
        migrations.AddField(
            model_name="networklocation",
            name="is_local",
            field=models.BooleanField(default=False),
        ),
    ]
