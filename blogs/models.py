from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
      return self.title + ":" + self.author


class Review(models.Model):
    rate = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    review = models.TextField(blank=True)
    created = models.DateTimeField()
    published = models.BooleanField(default=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
