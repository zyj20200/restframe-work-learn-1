from django.conf.urls import url,include
from app01 import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('books', views.BookView) # 注册book的url


app_name = 'app01'
urlpatterns = [
    url(r'',include(routers.urls)),# book的url
    url(r'^publishers/$', views.PublisherList.as_view()),
    url(r'^publishers/(?P<pk>\d+)/$', views.PublisherDetail.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^authors/$', views.AuthorList.as_view()),
]

# from app01 import views4 as view
# app_name = 'app01'
# urlpatterns = [
#     url(r'^publishers/$', views.PublisherView.as_view({'get': 'list', 'post': 'create'})),
#     url(r'^publishers/(?P<pk>\d+)/$', views.PublisherView.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     })),
# ]
