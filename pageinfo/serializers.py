from rest_framework import serializers
from .pageinfo import PageInfo

class PageInfoSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=1024)
    title = serializers.CharField( allow_blank=True, max_length=256, required=False)
    desc = serializers.CharField( allow_blank=True, max_length=2048, required=False )
    keywords = serializers.CharField( allow_blank=True, max_length=1024, required=False )

    def create(self, validated_data):
        return PageInfo( **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
