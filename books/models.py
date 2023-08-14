import uuid
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = f"author_{uuid.uuid4()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categeoryname = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = f"Category_{uuid.uuid4()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Categeoryname
    

class Book(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    publish_date = models.DateField()
    cover_image = models.ImageField(upload_to="covers/", blank=True, null=True)
    category = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author)
    stock = models.PositiveBigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = f"Book_{uuid.uuid4()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
