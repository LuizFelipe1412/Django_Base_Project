# Generated by Django 5.0.4 on 2024-05-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardobjectmodel',
            name='linked_plots',
            field=models.ManyToManyField(blank=True, null=True, through='dash.DashboardPlotObjectModel', to='dash.plotobjectmodel'),
        ),
    ]
