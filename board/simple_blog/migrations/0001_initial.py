# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('protected', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publish date')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publish date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_blog.Category')),
            ],
        ),
    ]