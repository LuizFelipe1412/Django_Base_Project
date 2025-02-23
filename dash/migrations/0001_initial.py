# Generated by Django 5.0.4 on 2024-05-07 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardObjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(to='auth.group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DashboardFilterObjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dash.dashboardobjectmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DashboardPlotObjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dash.dashboardobjectmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterObjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('dashboards', models.ManyToManyField(related_name='filters', through='dash.DashboardFilterObjectModel', to='dash.dashboardobjectmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dashboardfilterobjectmodel',
            name='filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dash.filterobjectmodel'),
        ),
        migrations.CreateModel(
            name='PlotObjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('datasource', models.JSONField()),
                ('widget_size', models.IntegerField()),
                ('groups', models.ManyToManyField(to='auth.group')),
                ('linked_dashboards', models.ManyToManyField(related_name='plots', through='dash.DashboardPlotObjectModel', to='dash.dashboardobjectmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dashboardplotobjectmodel',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dash.plotobjectmodel'),
        ),
        migrations.AddField(
            model_name='dashboardobjectmodel',
            name='linked_plots',
            field=models.ManyToManyField(through='dash.DashboardPlotObjectModel', to='dash.plotobjectmodel'),
        ),
    ]
