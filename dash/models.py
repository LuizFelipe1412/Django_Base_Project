from django.db import models
from django.contrib.auth.models import Group

from core.src.models import BaseModel


class PlotObjectModel(BaseModel):    
    name = models.CharField(max_length=255)
    datasource = models.JSONField()
    linked_dashboards = models.ManyToManyField(
        'DashboardObjectModel',
        related_name='plots',
        through='DashboardPlotObjectModel')
    widget_size = models.IntegerField()
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name


class FilterObjectModel(BaseModel):
    name = models.CharField(max_length=255)
    dashboards = models.ManyToManyField(
        'DashboardObjectModel',
        related_name='filters',
        through='DashboardFilterObjectModel')
    
    def __str__(self):
        return self.name
    

class DashboardObjectModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    groups = models.ManyToManyField(Group)
    linked_plots = models.ManyToManyField(PlotObjectModel, through='DashboardPlotObjectModel', null=True, blank=True)

    def __str__(self):
        return self.name


class DashboardFilterObjectModel(BaseModel):
    dashboard = models.ForeignKey(DashboardObjectModel, on_delete=models.PROTECT)
    filter = models.ForeignKey(FilterObjectModel, on_delete=models.PROTECT)


class DashboardPlotObjectModel(BaseModel):
    dashboard = models.ForeignKey(DashboardObjectModel, on_delete=models.PROTECT)
    plot = models.ForeignKey(PlotObjectModel, on_delete=models.PROTECT)