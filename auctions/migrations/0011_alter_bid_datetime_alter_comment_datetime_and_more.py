# Generated by Django 4.0.4 on 2022-05-23 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_bid_datetime_alter_comment_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 9, 11, 54, 289311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 9, 11, 54, 289311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 9, 11, 54, 288316, tzinfo=utc)),
        ),
    ]
