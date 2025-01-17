# Generated by Django 4.2.1 on 2025-01-11 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechnicalForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_no', models.CharField(max_length=100)),
                ('work_order_date', models.DateField()),
                ('project_plan', models.TextField()),
                ('due_date', models.DateField()),
                ('additional_info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScopeOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('technical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_of_work', to='technical.technicalform')),
            ],
        ),
        migrations.CreateModel(
            name='PTMRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField()),
                ('technical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ptm_roles', to='technical.technicalform')),
            ],
        ),
        migrations.CreateModel(
            name='PTLRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField()),
                ('technical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ptl_roles', to='technical.technicalform')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('technical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_team_members', to='technical.technicalform')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTeamLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('technical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_team_leaders', to='technical.technicalform')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('technical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_status', to='technical.technicalform')),
            ],
        ),
    ]
