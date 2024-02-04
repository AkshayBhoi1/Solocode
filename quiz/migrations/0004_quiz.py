# Generated by Django 4.0.3 on 2022-03-30 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_delete_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='duration of the quiz in minutes')),
                ('required_score_to_pass', models.IntegerField(help_text='required score in %')),
            ],
        ),
    ]
