# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 01:00
from __future__ import unicode_literals

import caching.base
import datetime
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_live', models.BooleanField(default=True, verbose_name='Display on site')),
                ('show_in_lists', models.BooleanField(default=True, verbose_name='Show in lists')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('pubdate', models.DateTimeField(default=datetime.datetime.now)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, help_text='Resized to fit 100% column width in template', null=True, upload_to='img/uploads/guide_images')),
                ('image_caption', models.TextField(blank=True)),
                ('image_credit', models.CharField(blank=True, help_text='Optional. Will be appended to end of caption in parens. Accepts HTML.', max_length=128)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('summary', models.TextField(blank=True, help_text='The two-sentence version of description, to be used on list pages.')),
                ('cover_color', models.CharField(blank=True, help_text='Hex code for background color of title card, e.g. `#256188`. Probably sampled from cover image.', max_length=32)),
            ],
            options={
                'ordering': ('-pubdate', 'title'),
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GuideArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('external_url', models.URLField(blank=True, help_text='Paste a URL here to link to an article elsewhere (overrides `Article` URL above).', null=True)),
                ('external_title', models.CharField(blank=True, help_text='Display title for link to article elsewhere (overrides `Article` title above).', max_length=128)),
                ('order', models.PositiveIntegerField(blank=True, db_index=True, default=1, help_text="A '1' will appear first, a '2' will appear second, and so on.")),
                ('article_notes', models.TextField(blank=True, help_text='Optional field for telling readers why this article is part of this guide.')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guides.Guide')),
            ],
            options={
                'verbose_name': 'Guide Article',
                'ordering': ('guide', 'order'),
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
    ]