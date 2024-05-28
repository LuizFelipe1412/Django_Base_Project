from typing import Any
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection

from json import dumps

from core.src.views import BaseHomeView, BaseCreateView, BaseShowView
from dash.models import DashboardObjectModel, PlotObjectModel
from dash.forms import DashboardObjectForm, DashboardObjectFormRetrive, PlotObjectForm, PlotObjectFormRetrive


def get_table_list():
    with connection.cursor() as cursor:
        table_list = connection.introspection.table_names(cursor)
    return table_list


def get_column_names(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
        return [desc[0] for desc in cursor.description]
        
class HomeDashboard(BaseHomeView):
    model = DashboardObjectModel
    context = 'dashboards'

    def get_queryset(self):
        return DashboardObjectModel.objects.prefetch_related('linked_plots', 'groups').order_by('pk')
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'dashboards'
        context['url_detail'] = 'dash-detail'
        return context


class CreateDashboard(BaseCreateView):
    model = DashboardObjectModel
    form_class = DashboardObjectForm


class ShowDashboard(BaseShowView):
    model = DashboardObjectModel
    form_class = DashboardObjectFormRetrive


class HomePlot(BaseHomeView):
    model = PlotObjectModel

    def get_queryset(self):
        return PlotObjectModel.objects.prefetch_related('linked_dashboards', 'groups').order_by('pk')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'plots'
        context['url_detail'] = 'plot-detail'
        return context


class CreatePlot(BaseCreateView):
    model = PlotObjectModel
    form_class = PlotObjectForm
    reverse_redirect = 'plot-detail'
    

class ShowPlot(BaseShowView):
    model = PlotObjectModel
    form_class = PlotObjectFormRetrive


# @login_required(login_url='login')
def home_dash(request):
    json_test = {
        'labels': ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho'],
        'datasets': [1,2,3,4,5,6,7]
    }

    chart_builder = (
        {
            'type': 'line',
            'size_in_cols': 6,
            'id_name': 'line_test',
            'data': {
                'labels': json_test['labels'],
                'datasets': {
                    'label': 'Dataset 1',
                    'data': json_test['datasets'],
                    'fill': False,
                    'borderColor': 'rgb(54, 162, 235)',
                    'lineTension': 0.1
                }
            },
                'options': {
                    'maintainAspectRatio': False,
                    'responsive': True,
            }
        },
        {
            'type': 'bar',
            'size_in_cols': 6,
            'id_name': 'bar_test',
            'data': {
                'labels': json_test['labels'],
                'datasets': {
                    'label': 'Dataset 1',
                    'data': json_test['datasets'],
                    # 'fill': False,
                    'borderColor': 'rgb(75, 192, 192)',
                    'backgroundColor': [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
                    ],
                    'lineTension': 0.1
                }
            },
            'options': {
                'maintainAspectRatio': False,
                'responsive': True,
            }
        },
        {
            'type': 'pie',
            'size_in_cols': 9,
            'id_name': 'pie_test',
            'data': {
                'labels': json_test['labels'],
                'datasets': {
                    'label': 'Dataset 1',
                    'data': json_test['datasets'],
                    # 'fill': False,
                    'borderColor': [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
                    ],
                    'backgroundColor': [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
                    ],
                    'lineTension': 0.1
                }
            },
            'options': {
                'maintainAspectRatio': False,
                'responsive': True,
            }
        }
    )

    return render(
        request,
        'dash.show.html' if True else 'chartjs.html',
        {
            'json_test': dumps(json_test),
            'chart_builder': dumps(chart_builder),
        }
    )


