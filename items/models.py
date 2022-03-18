from django.db import models
from seller.models import Brand,Category
# Create your models here.
#saving the user details
class CreatingUser(models.Model):

    first_name=models.CharField(primary_key=True,max_length=32)
    last_name=models.CharField(max_length=32,null=True)
    userName=models.CharField(max_length=32,null=True)
    passWord=models.CharField(max_length=32,null=True)
    email_address=models.EmailField(max_length=32,null=True)
    mobileNumber=models.IntegerField(null=True)
    def __str__(self):
        return self.first_name
#saving the product details

class itemsList(models.Model):
    brandSelection=models.ForeignKey(Brand,on_delete=models.CASCADE,db_constraint=False)
    categorySelection=models.ForeignKey(Category,on_delete=models.CASCADE,db_constraint=False)
    title=models.CharField(max_length=254)
    testcase=models.TextField()
    imageofproduct= models.ImageField(upload_to='images')
