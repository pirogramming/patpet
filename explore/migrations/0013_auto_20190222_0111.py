# Generated by Django 2.1.5 on 2019-02-22 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0012_auto_20190221_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communicationcomment',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='communicationcomment',
            name='message',
        ),
        migrations.AddField(
            model_name='communicationcomment',
            name='content',
            field=models.TextField(default='', verbose_name='내용'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='communicationcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
