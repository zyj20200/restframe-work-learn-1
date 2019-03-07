from django.conf.urls import url
from app02 import views


app_name = 'app02'
urlpatterns = [
    url(r'^projects/$', views.ProjectsList.as_view()),

]