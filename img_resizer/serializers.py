from rest_framework import serializers
from img_resizer.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'url', 'picture', 'width', 'height', 'parent_picture']

    def create(self, validated_data):
        return Image.objects.create(**validated_data)