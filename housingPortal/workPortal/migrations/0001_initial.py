# Generated by Django 4.2.17 on 2024-12-09 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workers', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=1024)),
                ('description', models.TextField(max_length=1024)),
                ('HousingArea', models.TextField(choices=[('Bedroom', 'bedroom'), ('Bathroom', 'bathroom'), ('Living Room', 'living room'), ('Kitchen', 'kitchen'), ('Laundry Room', 'laundry room'), ('Garage', 'garage'), ('Yard', 'yard')])),
                ('pictures', models.ImageField(upload_to='')),
                ('notes', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.communityaddresses')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workers.worker')),
            ],
        ),
    ]
