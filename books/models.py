from django.db import models
from authors.models import Author


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author_id = models.ManyToManyField(to=Author, on_delete=models.PROTECT)
    publisher = models.CharField(max_length=50)
    publish_date = models.DateField(max_length=50)
    category_id = models.ManyToManyField(to=Category, related_name='books', related_query_name='books')
    price = models.FloatField(max_length=10)
    sold_count = models.IntegerField(max_length=10)
