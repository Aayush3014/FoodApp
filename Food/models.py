from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):

    def __str__(self):  # This method is used to show item by its name in the Query Set.
        return self.item_name

    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500, default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/media/985748436085f06bb2bd63686ff491a5.jpg")


    def get_absolute_url(self):
        return reverse("Food:detail", kwargs={"pk": self.pk})