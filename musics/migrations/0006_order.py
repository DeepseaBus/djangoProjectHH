# Generated by Django 3.2.14 on 2022-08-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0005_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.TextField(default='customer')),
                ('bill', models.IntegerField(default=0)),
                ('orderNumber', models.TextField(max_length=6)),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]