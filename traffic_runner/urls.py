from django.conf.urls import url, patterns
from traffic_runner import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^plans/$', views.plans, name='plans'),
    url(r'^plan/$', views.plan, name='add_plan'),
    url(r'^plan/(?P<plan_id>\d+)/$', views.plan, name='edit_plan')
)