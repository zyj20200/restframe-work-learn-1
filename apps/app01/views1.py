from app01.models import *
from app01.serializer import PublishModelSerializer, BookModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


############################################
## 基于APIView


# 处理多条数据(查，增)
class PublisherView(APIView):
    # 查看多条数据
    def get(self, request):
        publishers_list = Publish.objects.all()
        publishers_list_serializer = PublishModelSerializer(publishers_list, many=True)
        return Response(publishers_list_serializer.data)
    # 添加数据
    def post(self, request):
        post_data = PublishModelSerializer(data=request.data)
        if post_data.is_valid():
            post_data.save()
            return Response(post_data.data)
        return Response(post_data.errors)


# 处理单条数据（查，改，删）
class PublisherDetailView(APIView):
    # 获取单条数据 get 请求
    def get(self, request, pk):
        publisher = Publish.objects.get(pk=pk)
        publisher_serializer = PublishModelSerializer(publisher)
        return Response(publisher_serializer.data)

    # 修改单条数据 put 请求
    def put(self, request, pk):
        # 获取数据
        publisher = Publish.objects.get(pk=pk)
        # 用新数据序列化原数据
        publisher_ser = PublishModelSerializer(publisher, data=request.data)
        # 如果数据合法，则保存数据
        if publisher_ser.is_valid():
            publisher_ser.save()
            # 返回新数据
            return Response(publisher_ser.data)
        return Response(publisher_ser.errors)

    def delete(self, request, pk):
        Publish.objects.get(pk=pk).delete()
        return Response()


class BookView(APIView):

    def get(self, request):
        books_list = Book.objects.all()
        books_list_serializer = BookModelSerializer(books_list, many=True)

        return Response(books_list_serializer.data)

    def post(self, request):
        post_data = BookModelSerializer(data=request.data)
        if post_data.is_valid():
            post_data.save()
            return Response(post_data.data)
        return Response(post_data.errors)
