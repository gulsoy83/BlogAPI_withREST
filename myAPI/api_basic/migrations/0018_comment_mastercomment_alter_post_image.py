# Generated by Django 4.2.1 on 2023-07-16 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0017_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='masterComment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_linkedtomasterComment', to='api_basic.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_api/'),
        ),
    ]