from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    """Model representing a book genre."""

    name = models.CharField(max_length=10, default="DEFAULT")
    quantity = models.IntegerField()
    aisle = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name + "(" + str(self.quantity) + " available at $" + str(self.price) + ")"

class List(models.Model):
    listname = models.CharField(max_length=100, default="DEFAULT")
    item = models.ManyToManyField(Item)

class UserModel(models.Model):
    username = models.CharField(max_length=100, default="DEFAULT")
    favoriteCart = models.ForeignKey(List, on_delete=models.SET_NULL, null=True)
    favoriteItems = models.ManyToManyField(Item)

class Store(models.Model):
    storename = models.CharField(max_length=100, default="DEFAULT")
    items = models.ManyToManyField(Item)
    def __str__(self):
        """String for representing the Model object."""
        return self.storename