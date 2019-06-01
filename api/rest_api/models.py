from django.db import models

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mail = models.EmailField()

    def __str__(self):
        return str(self.name + " " + self.surname)

class Post(models.Model):
    text = models.TextField(max_length=3500)
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.IntegerField()

    def __str__(self):
        return self.slug
