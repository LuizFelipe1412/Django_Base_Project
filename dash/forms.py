from django import forms
from .models import DashboardObjectModel, PlotObjectModel

class DashboardObjectForm(forms.ModelForm):
    template_name = 'create.form.html'
    class Meta:
        model = DashboardObjectModel
        fields = ('name', 'active', 'description', 'linked_plots', 'groups')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'linked_plots': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            
        }


class DashboardObjectFormRetrive(DashboardObjectForm):
    class Meta(DashboardObjectForm.Meta):
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'readonly': True}),
            'linked_plots': forms.SelectMultiple(attrs={'class': 'form-control', 'readonly': True}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control', 'readonly': True}),
        }


class PlotObjectForm(forms.ModelForm):
    template_name = 'create.form.html'
    class Meta:
        model = PlotObjectModel
        fields = ('name', 'datasource', 'linked_dashboards', 'widget_size', 'groups')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'datasource': forms.Textarea(attrs={'class': 'form-control'}),
            'linked_dashboards': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'widget_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class PlotObjectFormRetrive(PlotObjectForm):
    class Meta(PlotObjectForm.Meta):
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'datasource': forms.Textarea(attrs={'class': 'form-control', 'readonly': True}),
            'linked_dashboards': forms.SelectMultiple(attrs={'class': 'form-control', 'readonly': True}),
            'widget_size': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control', 'readonly': True}),
        }