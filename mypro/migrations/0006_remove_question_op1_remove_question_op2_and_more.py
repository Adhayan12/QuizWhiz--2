# Generated by Django 5.1.4 on 2025-01-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypro', '0005_rename_quiz_title_quizresult_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='op1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op4',
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.JSONField(default=list),
        ),
    ]
