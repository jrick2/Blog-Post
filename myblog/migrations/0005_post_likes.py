# Generated by Django 4.1 on 2022-08-24 18:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myblog", "0004_category_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="blog_post", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
