# Generated by Django 2.1.7 on 2019-04-21 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='website.SearchItem'),
        ),
    ]
