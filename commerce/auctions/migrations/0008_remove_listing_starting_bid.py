# Generated by Django 5.0.7 on 2024-08-15 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_rename_bid_listing_starting_bid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='starting_bid',
        ),
    ]
