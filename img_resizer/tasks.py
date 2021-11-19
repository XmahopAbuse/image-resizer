
from resize.celery import app
from django.conf import settings
from rest_framework import status
import PIL.Image
from img_resizer.models import Image
from img_resizer.serializers import ImageSerializer

def resize_img(request, image):
    try:
        new_width = request.data['width'] if request.data['width'] else image.width
        new_height = request.data['height'] if request.data['height'] else image.height

        new_size = (int(new_width), int(new_height))

        original_image = PIL.Image.open(image.picture)
        resized_image = original_image.resize(new_size)
        resized_image.save(settings.MEDIA_ROOT + "/" + str(new_size) + image.name)


        new_image = Image(picture=str(new_size) + image.name,parent_picture=image.id)
        new_image.save()

        serializer = ImageSerializer(new_image)

        data = {"data": serializer.data, "status":status.HTTP_201_CREATED}

    except Exception as e:
        data = {"data": e, "status": status.HTTP_400_BAD_REQUEST}

    return data