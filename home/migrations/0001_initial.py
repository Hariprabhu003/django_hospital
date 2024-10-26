# Generated by Django 5.0.3 on 2024-03-24 15:40

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appoitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('select_doctor', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'appoitment',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.models.getFileName)),
                ('department', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'doctor_details',
            },
        ),
    ]
