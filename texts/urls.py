from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'translate/$', views.translate, name='translate'),
    url(r'^error/$', views.error_report, name='error_report'),
]