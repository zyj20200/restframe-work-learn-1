from app02.models import Projects,Department,City,Profession,ProjectSet
from rest_framework import serializers

class ProjectsSerializers(serializers.Serializer):
    limit = serializers.IntegerField(required=False)
    city = serializers.CharField(max_length=32 ,required=False)
    department = serializers.CharField(max_length=32, required=False)
    profession = serializers.CharField(max_length=32, required=False)
    p_set = serializers.CharField(max_length=32, required=False)


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

        depth = 1


