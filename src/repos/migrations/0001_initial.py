# Generated by Django 4.2.6 on 2023-10-17 15:57

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateRepos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('repos', models.CharField(max_length=100, verbose_name='仓库地址')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, base.models.IDHandler),
        ),
    ]