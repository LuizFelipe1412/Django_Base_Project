# Generated by Django 5.0.4 on 2024-05-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_alter_dashboardobjectmodel_linked_plots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardfilterobjectmodel',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='dashboardobjectmodel',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='dashboardplotobjectmodel',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='filterobjectmodel',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='plotobjectmodel',
            name='metadata',
        ),
    ]
