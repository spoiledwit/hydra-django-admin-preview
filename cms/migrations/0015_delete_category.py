# Generated by Django 5.0.6 on 2024-08-22 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_alter_blog_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
