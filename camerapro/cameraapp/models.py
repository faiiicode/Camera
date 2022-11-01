from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Product(models.Model):

    name=models.CharField(max_length=250,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField(upload_to='product',blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__ (self):
     return '{}'.format(self.name)


    class Meta:
      ordering= ('name',)
      verbose_name='product'
      verbose_name_plural='products'

class Review(models.Model):
    name = models.CharField(max_length=250, unique=True)
    desc=models.CharField(max_length=300,unique=True)
    image=models.ImageField(upload_to='founders',blank=True)

    def __str__ (self):
     return '{}'.format(self.name)


    class Meta:
      ordering= ('name',)
      verbose_name='Founder'
      verbose_name_plural='Founders'


class Callback(models.Model):

    name=models.CharField(max_length=50, unique=False)
    email=models.EmailField(max_length=100,blank=False,unique=False)
    Phone=models.CharField(max_length=50)
    message=models.TextField()



    def __str__ (self):
     return '{}'.format(self.name)


    class Meta:
      ordering= ('name',)
      verbose_name='Call Back form'
      verbose_name_plural='Call Back Forms'




class mailstore(models.Model):

    email=models.EmailField(max_length=100,blank=False,unique=False)




    def __str__ (self):
     return '{}'.format(self.email)

    class Meta:
      ordering= ('email',)
      verbose_name='Newsleter mails'
      verbose_name_plural='Newsletter mails'

