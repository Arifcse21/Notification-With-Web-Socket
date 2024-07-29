from echowave.apps import EchowaveConfig
from django.urls import re_path
from django.views.generic import TemplateView

app_name = EchowaveConfig.name
urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="echowave/index.html"), name='echowave'),
]