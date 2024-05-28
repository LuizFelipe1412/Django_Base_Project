from typing import Any

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models.query import QuerySet
from django.forms import model_to_dict

from core.settings import PROJECT_NAME_SUFFIX

def login(request):

    return render(
        request,
        'auth/login.html',
        {
            'project_name_suffix': PROJECT_NAME_SUFFIX
        })


class BaseHomeView(ListView):
    template_name = 'dash.index.html'
    context_object_name = 'objects'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().order_by('pk')


class BaseCreateView(CreateView):
    """
    reverse_redirect: str. Name of the url to redirect after create a new object.
    """
    template_name = 'dash.create.html'
    reverse_redirect = None
    
    def get_success_url(self) -> str:
        return reverse(self.reverse_redirect, kwargs={'pk': self.object.pk})


class BaseShowView(FormMixin, DetailView):
    template_name = 'dash.detail.html'
    context_object_name = 'object'

    def get_initial(self) -> dict[str, Any]:
        initial_data = super().get_initial()
        initial_data.update(model_to_dict(self.object))
        return initial_data
    
    def form_valid(self, form):
        return super().form_valid(form)