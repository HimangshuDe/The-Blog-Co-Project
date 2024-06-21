# Generated by Django 5.0.6 on 2024-06-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
