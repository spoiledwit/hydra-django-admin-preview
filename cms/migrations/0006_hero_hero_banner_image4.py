# Generated by Django 5.0.6 on 2024-07-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_remove_hero_hero_image4'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_banner_image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
