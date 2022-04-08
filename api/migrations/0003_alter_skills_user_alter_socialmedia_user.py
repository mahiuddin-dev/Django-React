# Generated by Django 4.0.3 on 2022-04-08 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_user_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='api.person'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media', to='api.person'),
        ),
    ]