# Generated by Django 4.0.3 on 2022-04-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_remove_javaquiz_option1_remove_javaquiz_option2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cppaccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Javaacces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Jsaccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Phpaccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pythonaccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=1)),
            ],
        ),
    ]
