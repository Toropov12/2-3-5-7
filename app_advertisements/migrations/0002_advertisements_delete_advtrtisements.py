# Generated by Django 4.2.3 on 2023-08-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('auction', models.BooleanField(verbose_name='Торг')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')),
            ],
        ),
        migrations.DeleteModel(
            name='Advtrtisements',
        ),
    ]