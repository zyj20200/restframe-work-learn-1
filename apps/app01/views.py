from app01.models import *
# from app01.utils import SVIPPermission
from app01.utils import AuthToken, SVIPPermission, Thorttle
from app01.serializer import PublishModelSerializer, BookModelSerializer, AuthorModelSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


# eec1fd859b89b9d62d37c38795ece055
# 97f6c1d71c83ae2c714cf451dd0a074b

# 分页
class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    page_size_query_param = "size"
    max_page_size = 5

# 分页
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1


class AuthorList(APIView):
    def get(self, request):

        ######################## 获取get 请求时的参数 ################
        #  http://127.0.0.1:8000/authors/?limit=1&offset=1
        from .serializer import AuthorSerializer
        aa = AuthorSerializer(data=request.query_params)
        print(aa)
        # aa:data=<QueryDict: {'offset': ['1'], 'limit': ['1']}>
        ######################## 获取get 请求时的参数 ################

        author_list = Author.objects.all()
        # 分页
        # paginate = MyPageNumberPagination()
        paginate = MyLimitOffsetPagination()
        author_list_paged = paginate.paginate_queryset(queryset=author_list, request=request, view=self)
        # 序列化
        author_list_s = AuthorModelSerializer(author_list_paged, many=True)
        return Response(author_list_s.data)


# 查看多条&添加 publisher
class PublisherList(generics.ListCreateAPIView):
    # 认证三部曲
    # authentication_classes = [AuthToken, ]
    # permission_classes = [SVIPPermission,]
    # throttle_classes = [Thorttle,]
    pagination_class = MyPageNumberPagination

    queryset = Publish.objects.all()
    serializer_class = PublishModelSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishModelSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = MyPageNumberPagination

# 生成随机字符串
def get_random_str(user):
    import hashlib, time
    ctime = str(time.time())
    md5 = hashlib.md5(bytes(user, encoding="utf8"))
    md5.update(bytes(ctime, encoding="utf8"))
    return md5.hexdigest()


# 自定义登录认证
class LoginView(APIView):
    def post(self, request):
        res = {'code': 1000, 'msg': None}
        username = request.data.get('username')
        pwd = request.data.get('pwd')
        user_obj = User.objects.filter(username=username, pwd=pwd).first()
        if user_obj:
            random_str = get_random_str(username)
            token = Token.objects.update_or_create(user=user_obj, defaults={"token": random_str})
            res['token'] = random_str
            res['msg'] = '登录成功'
        else:
            res['code'] = 404
            res['msg'] = '登录失败'
        return Response(res)
