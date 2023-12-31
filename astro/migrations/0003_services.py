# Generated by Django 4.2.4 on 2023-09-03 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('astro', '0002_horoscope'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(default='deafault.jpeg', upload_to='client')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
