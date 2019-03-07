from app01.models import *
from app01.serializer import PublishModelSerializer, BookModelSerializer

from rest_framework import viewsets


############################################
## 基于 viewsets.ModelViewSet


# 多条数据和单挑数据的处理合二为一
class PublisherView(viewsets.ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishModelSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
