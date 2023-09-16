from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta: 
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_new = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    seller = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    # likes
    # comments
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name