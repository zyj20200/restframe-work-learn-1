from app02.models import *
from app02.serializer import ProjectsModelSerializer,ProjectsSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class ProjectsList(APIView):
    @staticmethod
    def condition_filter(request,queryset):
        '''
        获取请求参数，根据参数回去数据
        queryset默认为所有数据
        '''
        if request.query_params:
            # 根据参数中city的值（宁波），从city表中，获取该值对应的对象，用来获取其id值
            city = City.objects.filter(city=request.query_params.get("city", None)).first()
            department = Department.objects.filter(department=request.query_params.get("department", None)).first()
            profession = Profession.objects.filter(profession=request.query_params.get("profession", None)).first()
            p_set = ProjectSet.objects.filter(p_set=request.query_params.get("p_set", None)).first()

            # 如果
            if city:#宁波
                queryset = queryset.filter(city=city.id)
            if department:
                queryset = queryset.filter(department=department.id)
            if profession:
                queryset = queryset.filter(profession=profession.id)
            if p_set:
                queryset = queryset.filter(p_set=p_set.id)
        return queryset


    def get(self, request):
        # 1.解析请求参数
        serializer = ProjectsSerializers(data=request.query_params)
        # 2.如果请求参数合法
        if serializer.is_valid():
            # 3.根据请求参数，获取数据
            data_queryset = self.condition_filter(request, Projects.objects.all())
            # 分页
            page = LimitOffsetPagination()
            data_paged = page.paginate_queryset(queryset=data_queryset, request=request, view=self)
            # 数据序列化
            data_s = ProjectsModelSerializer(data_paged, many=True).data
            return Response(data_s)
        else:
            return Response(serializer.errors)




