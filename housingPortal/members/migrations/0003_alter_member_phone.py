# Generated by Django 4.2.17 on 2024-12-09 17:40

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_communityaddresses_options_member_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]