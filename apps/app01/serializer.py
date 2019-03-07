from app01.models import *

from rest_framework import serializers
from rest_framework.serializers import Serializer


class PublishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32, required=False)
    age = serializers.IntegerField(required=False)


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
