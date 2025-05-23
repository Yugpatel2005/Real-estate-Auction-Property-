# Generated by Django 5.1.6 on 2025-03-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_property_carpet_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='reigstermodel',
            name='id_proof',
            field=models.FileField(blank=True, default=None, null=True, upload_to='id_proofs/'),
        ),
        migrations.AddField(
            model_name='reigstermodel',
            name='role',
            field=models.CharField(choices=[('User', 'User'), ('Seller', 'Seller')], default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reigstermodel',
            name='status',
            field=models.CharField(choices=[('0', 'unapproved'), ('1', 'approved')], default='0', max_length=10),
        ),
    ]
