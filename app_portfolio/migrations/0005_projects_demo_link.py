# Generated by Django 4.1.13 on 2024-02-18 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0004_home_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='demo_link',
            field=models.URLField(blank=True),
        ),
    ]
