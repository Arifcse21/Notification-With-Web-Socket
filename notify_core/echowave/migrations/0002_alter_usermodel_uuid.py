# Generated by Django 5.0.7 on 2024-07-16 06:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echowave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=255, unique=True),
        ),
    ]
