# Generated by Django 5.0.6 on 2024-08-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerstories',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
