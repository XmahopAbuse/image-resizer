# Generated by Django 3.2.9 on 2021-11-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_resizer', '0002_alter_image_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
