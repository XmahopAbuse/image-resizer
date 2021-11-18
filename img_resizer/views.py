from django.core.exceptions import FieldError
import requests
from img_resizer.models import Image
from rest_framework import viewsets
from img_resizer.serializers import ImageSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
import PIL.Image
from django.conf import settings


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    @action(methods=['post'], detail=True)
    def resize(self, request, pk=None):
        
        image = self.get_object()
        try:
            new_width = request.data['width'] if request.data['width'] else image.width
            print(new_width)

            # original_image = PIL.Image.open(image.picture)
            # resized_image = original_image.resize((new_width, new_height))
            # resized_image.save(settings.MEDIA_ROOT + "/" + str((new_width, new_height)) + image.name)


            # new_image = Image(picture=resized_image, parent_picture=image.id)
            # new_image.save()

        except FieldError as e:
            return HttpResponse(e)
    

        return HttpResponse(image.id)