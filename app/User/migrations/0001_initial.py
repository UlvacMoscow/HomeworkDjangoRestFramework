# Generated by Django 2.1.5 on 2019-01-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=255, verbose_name='Почта')),
            ],
        ),
    ]
