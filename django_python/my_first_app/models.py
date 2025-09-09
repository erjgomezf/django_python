from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    colors = models.TextField(max_length=250, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.year} - {self.colors}"

class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.TextField(max_length=100)
    birthdate = models.DateField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) # Relacion uno a muchos
    authors = models.ManyToManyField(Author, related_name="authors") # Relacion muchos a muchos
    
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE) # Para relacion uno a uno
    website = models.URLField(max_length=200, null=True)
    bio = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return self.author.name