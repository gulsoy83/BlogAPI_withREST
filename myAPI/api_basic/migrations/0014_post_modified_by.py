# Generated by Django 4.2.1 on 2023-06-11 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_basic', '0013_rename_masterpost_comment_masterpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts_ownedbymodifieruser', to=settings.AUTH_USER_MODEL),
        ),
    ]