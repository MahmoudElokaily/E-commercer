from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=8,decimal_places=2)
    type = models.CharField(max_length=100)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE , related_name='products')
    slug = models.CharField(max_length=50,blank=True , null = True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name