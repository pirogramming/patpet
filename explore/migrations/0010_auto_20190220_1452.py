# Generated by Django 2.1.5 on 2019-02-20 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('explore', '0009_auto_20190220_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communicationpost',
            name='user',
        ),
        migrations.AddField(
            model_name='communicationpost',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
