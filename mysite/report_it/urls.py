from django.conf.urls import url
from report_it import views

urlpatterns = [
    url(r'^log/$', views.log, name='log'),
    url(r'^log/confirmation/$', views.confirmation, name='confirmation'),
    url(r'^$', views.index, name='index'),
] 