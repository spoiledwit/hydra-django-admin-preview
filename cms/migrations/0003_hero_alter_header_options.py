# Generated by Django 5.0.6 on 2024-07-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_header_menu_item_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(blank=True, max_length=100, null=True)),
                ('hero_description', models.TextField(blank=True, null=True)),
                ('hero_button_text', models.CharField(blank=True, max_length=100, null=True)),
                ('hero_button_link', models.CharField(blank=True, max_length=100, null=True)),
                ('hero_banner_image1', models.ImageField(upload_to='images/')),
                ('hero_banner_image2', models.ImageField(upload_to='images/')),
                ('hero_banner_image3', models.ImageField(upload_to='images/')),
                ('hero_image4', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Hero',
            },
        ),
        migrations.AlterModelOptions(
            name='header',
            options={'verbose_name_plural': 'Header'},
        ),
    ]
