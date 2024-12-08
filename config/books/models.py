from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField( upload_to='author/photos' ,blank=True,null=True)
    def __str__(self):
        return self.first_name
class Book(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date=models.DateField
    isbn=models.CharField(max_length=13,unique=True)
    genre=models.CharField(max_length=100)
    summary=models.TextField(blank=True,null=True)
    photo=models.ImageField(upload_to='book/photos', blank=True,null=True)
    def __str__(self):
        return self.title
