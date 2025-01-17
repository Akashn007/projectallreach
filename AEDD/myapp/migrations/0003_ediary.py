# Generated by Django 4.2.1 on 2024-12-19 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_followup'),
    ]

    operations = [
        migrations.CreateModel(
            name='EDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date_time', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ediary_entries', to='myapp.client')),
            ],
        ),
    ]
