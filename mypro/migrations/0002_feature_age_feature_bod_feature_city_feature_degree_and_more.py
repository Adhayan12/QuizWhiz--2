# Generated by Django 5.1.4 on 2024-12-31 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feature',
            name='bod',
            field=models.CharField(default='1st Jan, 2000', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='city',
            field=models.CharField(default='Lucknow', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='degree',
            field=models.CharField(default='B.tech', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='email',
            field=models.EmailField(default='adsri@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='phone',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
