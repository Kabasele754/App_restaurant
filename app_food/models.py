from django.db import models

# Create your models here.

# la classe categorie nouriture
class FoodCategory(models.Model):
    name = models.CharField(max_length=30)

#  la classe nourriture 
class Food(models.Model):
    # CREATE TABLE  
    name = models.CharField(max_length=30,null=False,blank=False,)
    price = models.IntegerField(default=1)
    image = models.ImageField(default="food/food.png")
    create = models.DateTimeField(auto_now_add=True) 
    update = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True,blank=True)
    publish = models.BooleanField(default=False)
    category = models.ForeignKey(FoodCategory,on_delete=models.CASCADE)




