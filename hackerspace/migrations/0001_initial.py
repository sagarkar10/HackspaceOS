# Generated by Django 2.2.6 on 2019-10-26 20:44

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_error_code', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('str_name', models.CharField(blank=True, max_length=250, null=True)),
                ('int_count', models.IntegerField(default=0)),
                ('text_description', models.TextField(blank=True, null=True)),
                ('text_description_no_numbers', models.TextField(blank=True, null=True)),
                ('json_context', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True)),
                ('boolean_fixed', models.BooleanField(default=False)),
                ('list_origins', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), blank=True, null=True, size=None)),
                ('list_dateUNIXtimes', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='last_updated')),
            ],
        ),
    ]