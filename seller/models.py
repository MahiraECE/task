from django.db import models

# Create your models here.
#DB to save Category details

class Category(models.Model):
    categoryName=models.CharField(max_length=254,primary_key=True)
    def __str__(self):
        return self.categoryName
#DB to save Brand details

class Brand(models.Model):
    brandCategory=models.ForeignKey(Category,on_delete=models.CASCADE)
    brandName=models.CharField(max_length=254,primary_key=True)
    imageofbrand= models.ImageField(upload_to='images')
    def __str__(self):
        return self.brandName