from django.core.exceptions import FieldError
import requests
from img_resizer.models import Image
from rest_framework import viewsets
from img_resizer.serializers import ImageSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
import PIL.Image
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from img_resizer import tasks


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    @action(methods=['post'], detail=True)
    def resize(self, request, pk=None):
        """Call celery task"""

        image = self.get_object()
        task = tasks.resize_img(request, image)
        return Response(data = task['data'], status=task['status'])


        