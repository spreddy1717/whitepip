from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile/",blank=True, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    uuid=models.UUIDField(primary_key=True)
    Categeoryname=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.Categeoryname
    
class Book(models.Model):
    uuid = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=1000)
    ISBN =  models.CharField(max_length=13,unique=True)
    summary= models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=7)
    publish_date=models.DateField()
    cover_image=models.ImageField(upload_to="covers/",blank=True,null=True)
    category = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author)
    stock=models.PositiveBigIntegerField()


    def __str__(self):
        return self.title
    