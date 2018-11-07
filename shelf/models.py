from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, )
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher, on_delete = models.DO_NOTHING,)
    def __str__(self):
        return self.title