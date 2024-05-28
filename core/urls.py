from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

from core.src.views import login
from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('', lambda request: JsonResponse({"msg":"Project Running..."})),
    path('sig/', include('sig.urls')),
    path('dash/', include('dash.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns