# Generated by Django 2.1.5 on 2019-02-18 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0007_auto_20190215_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]