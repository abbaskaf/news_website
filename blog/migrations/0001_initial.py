# Generated by Django 4.2.7 on 2023-11-29 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('active', models.BooleanField(verbose_name='active')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('thumbnail', models.ImageField(null=True, upload_to='posts/', verbose_name='thumb')),
                ('slug', models.SlugField(allow_unicode=True, unique_for_date='publish_time', verbose_name='slug')),
                ('lead', models.CharField(blank=True, max_length=1024, null=True, verbose_name='lead')),
                ('body', models.TextField(verbose_name='body')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updates', models.DateTimeField(auto_now=True, verbose_name='updates')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=15, verbose_name='status')),
                ('featured', models.BooleanField(null=True, verbose_name='featured')),
                ('publish_time', models.DateTimeField(blank=True, null=True, verbose_name='publish_time')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-publish_time'],
            },
        ),
    ]
