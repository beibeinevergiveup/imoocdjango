# Generated by Django 2.2.1 on 2019-07-19 06:33

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
                ('open_id', models.CharField(max_length=32, unique=True)),
                ('nickname', models.CharField(max_length=256)),
            ],
        ),
    ]