# Generated by Django 3.2.7 on 2021-09-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formpage1', '0005_auto_20210906_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionmodel',
            name='session_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
