# Generated by Django 5.1.6 on 2025-03-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_alter_property_listing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
