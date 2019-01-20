# Generated by Django 2.1.5 on 2019-01-20 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creater', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание:')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Customer', verbose_name='Заказчик')),
                ('decoration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item', verbose_name='Товар')),
            ],
        ),
    ]
