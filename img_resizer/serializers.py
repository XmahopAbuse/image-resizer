from rest_framework import serializers
from img_resizer.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def create(self, validated_data):
        return Image.objects.create(**validated_data)