from django.urls import path

from .views import *

urlpatterns = [
    path('example', home_dash, name='dash-home-test'),
    path('', HomeDashboard.as_view(), name='dash-home'),
    path('create', CreateDashboard.as_view(), name='dash-create'),
    path('<int:pk>', ShowDashboard.as_view(), name='dash-detail'),
    path('plots', HomePlot.as_view(), name='plot-home'),
    path('plots/create', CreatePlot.as_view(), name='plot-create'),
    path('plots/<int:pk>', ShowPlot.as_view(), name='plot-detail'),
]