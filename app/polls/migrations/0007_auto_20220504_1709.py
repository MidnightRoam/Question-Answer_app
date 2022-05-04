# Generated by Django 3.2 on 2022-05-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_rename_result_choice_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.BooleanField(default=False, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='correct_answer',
            field=models.BooleanField(default=False, verbose_name='correct answer'),
        ),
    ]
