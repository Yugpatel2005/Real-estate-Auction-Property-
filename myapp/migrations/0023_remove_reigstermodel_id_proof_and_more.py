# Generated by Django 5.1.6 on 2025-03-26 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_reigstermodel_id_proof_reigstermodel_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reigstermodel',
            name='id_proof',
        ),
        migrations.RemoveField(
            model_name='reigstermodel',
            name='role',
        ),
        migrations.RemoveField(
            model_name='reigstermodel',
            name='status',
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_property', to='myapp.reigstermodel'),
        ),
    ]
