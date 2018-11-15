from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("items_cart", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, {self.location}'

class Item(models.Model):
    name = models.CharField(max_length=20)
    store = models.ForeignKey("Store", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    aisle = models.IntegerField()
    short_description = models.CharField(max_length=150)
    item_number = models.IntegerField()

    class Meta:
        ordering = ["name", "item_number"]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("item-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, {self.item_number}'

class List(models.Model):
    listname = models.CharField(max_length=100, default="DEFAULT")
    item = models.ManyToManyField(Item)

class UserModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    favoriteCart = models.ForeignKey(List, on_delete=models.SET_NULL, null=True)
    favoriteItems = models.ManyToManyField(Item)
