# Generated by Django 4.1.5 on 2023-01-28 22:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_entradadeblog_cuerpo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entradadeblog",
            name="cuerpo",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]