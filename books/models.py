import json

from django.db import models
from authors.models import Author


class CommonInfoModel(models.Model):

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    class Meta:
        abstract = True


class Category(CommonInfoModel):
    category_id = models.CharField(max_length=15, primary_key=True)
    category_name = models.CharField(max_length=20)


class Book(CommonInfoModel):
    book_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=500)
    author = models.ForeignKey(to=Author, on_delete=models.PROTECT)
    publisher = models.CharField(max_length=50)
    publish_date = models.DateField()
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    price = models.FloatField()
    sold_count = models.IntegerField()
