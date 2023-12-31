# Generated by Django 4.2.1 on 2023-06-07 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pimage',
            field=models.ImageField(default='static/picture1.jpg', upload_to='profile/images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimage',
            field=models.ImageField(default='static/profile2.avif', upload_to='profile/images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
