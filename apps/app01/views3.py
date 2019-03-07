from app01.models import *
from app01.serializer import PublishModelSerializer, BookModelSerializer

from rest_framework import generics


############################################
## 基于通用的类的视图


# 处理多条数据(查，增)
class PublisherView(generics.ListCreateAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishModelSerializer

# 处理单条数据（查，改，删）
class PublisherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishModelSerializer


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
