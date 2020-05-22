from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

# class Location(models.Model):
#     location_name = models.CharField(max_length=30)


# class Images(models.Model):
#     image_path = models.ImageField(upload_to = 'images/')
#     name = models.CharField(max_length =30)
#     description = models.TextField()
#     location = models.ForeignKey(Location, on_delete=models.CASCADE,)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    