# Generated by Django 2.1.5 on 2019-02-17 06:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recommend',
            field=models.ManyToManyField(blank=True, related_name='recommended', to=settings.AUTH_USER_MODEL),
        ),
    ]