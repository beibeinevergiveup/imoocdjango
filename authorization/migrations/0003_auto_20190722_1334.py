# Generated by Django 2.2.1 on 2019-07-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_auto_20190719_2221'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['nickname'], name='authorizati_nicknam_b76290_idx'),
        ),
    ]