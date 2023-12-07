# Generated by Django 4.1.5 on 2023-12-07 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TimeManagementToolApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teht', models.TextField()),
                ('kurssi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeManagementToolApp.kurssi')),
            ],
        ),
    ]
