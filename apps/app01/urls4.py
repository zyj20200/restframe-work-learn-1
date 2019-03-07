from django.conf.urls import url
from app01 import views

app_name = 'app01'
urlpatterns = [
    url(r'^publishers/$', views.PublisherView.as_view({'get': 'list', 'post': 'create'})),
    url(r'^publishers/(?P<pk>\d+)/$', views.PublisherView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

]
