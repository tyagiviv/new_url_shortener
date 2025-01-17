# Generated by Django 3.0.10 on 2024-12-15 11:59

from django.db import migrations, models
import shortener_app.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0002_auto_20241215_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliasedUrl',
            fields=[
                ('alias', models.CharField(default=shortener_app.utils.get_random_alias, max_length=8, primary_key=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='urlAlias',
        ),
    ]
