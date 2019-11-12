# Generated by Django 2.2.6 on 2019-11-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0010_auto_20191109_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='guilde',
            name='url_wiki',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='machine',
            name='url_wiki',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='url_wiki',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='space',
            name='url_wiki',
            field=models.URLField(blank=True, null=True),
        ),
    ]