# Generated by Django 3.2.7 on 2021-09-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formpage1', '0002_auto_20210905_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('clientLead_id', models.IntegerField(primary_key=True, serialize=False)),
                ('iin', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField()),
                ('personal_data_success', models.BooleanField()),
                ('session_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='personlead_session_id', to='formpage1.sessionmodel')),
            ],
            options={
                'verbose_name': 'ИИН Lead',
                'verbose_name_plural': 'ИИН Leads',
            },
        ),
        migrations.DeleteModel(
            name='PersonLeads',
        ),
    ]
