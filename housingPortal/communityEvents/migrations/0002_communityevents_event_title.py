# Generated by Django 4.2.17 on 2024-12-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityEvents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityevents',
            name='event_title',
            field=models.TextField(max_length=25, null=True),
        ),
    ]
