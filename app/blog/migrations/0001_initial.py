# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-17 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('status', models.CharField(choices=[(b'd', b'\xe5\xbb\xb6\xe8\xbf\x9f\xe5\x8f\x91\xe5\xb8\x83'), (b'p', b'\xe5\x8f\x91\xe5\xb8\x83')], max_length=1, verbose_name='\u6587\u7ae0\u72b6\u6001')),
                ('abstract', models.CharField(blank=True, help_text='\u53ef\u9009\u9879\uff0c\u82e5\u4e3a\u7a7a\u5219\u6458\u53d6\u6b63\u6587\u94b154\u4e2a\u5b57\u7b26', max_length=54, null=True, verbose_name='\u6458\u8981')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='\u70b9\u8d5e\u6570')),
                ('topped', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-updated'],
                'db_table': 'blog_article',
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='\u8bc4\u8bba\u8005\u540d\u5b57')),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='\u8bc4\u8bba\u6240\u5c5e\u6587\u7ae0')),
            ],
            options={
                'db_table': 'blog_comment',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u7c7b\u540d')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'db_table': 'blog_category',
            },
        ),
        migrations.CreateModel(
            name='Suggest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200, verbose_name='\u610f\u89c1')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'blog_suggest',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u6807\u7b7e\u540d')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'db_table': 'blog_tag',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='\u6587\u7ae0\u6807\u7b7e\uff0c\u591a\u9009', related_name='tag_set', related_query_name='article', to='blog.Tag', verbose_name='\u6807\u7b7e\u96c6\u5408'),
        ),
    ]
