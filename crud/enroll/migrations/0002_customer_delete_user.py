# Generated by Django 4.0.4 on 2022-05-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=72)),
                ('email', models.EmailField(max_length=72)),
                ('password', models.CharField(max_length=72)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
