# Generated by Django 5.0.6 on 2024-07-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_rename_user_id_usermodel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
