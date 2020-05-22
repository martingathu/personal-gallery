from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def get_category(cls):
        category = cls.objects.all()
        return category

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        locations = cls.objects.all()
        return locations


class Images(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def save_images():
        self.save()

    def delete_images():
        self.delete()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_word):
        photos = cls.objects.filter(category__category_name__icontains=search_word)

        return photos

    @classmethod
    def get_by_location(cls, location):
        images = Images.objects.filter(location__location_name__icontains=location).all()

        return images
