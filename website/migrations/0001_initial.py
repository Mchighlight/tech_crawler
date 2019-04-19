# Generated by Django 2.1.7 on 2019-04-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'search item',
                'verbose_name_plural': 'search item',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('search_item', models.ManyToManyField(to='website.SearchItem')),
            ],
            options={
                'verbose_name': 'website content',
                'verbose_name_plural': 'webstie content',
            },
        ),
    ]