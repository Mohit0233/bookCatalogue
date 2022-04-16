from django.db import models


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=20)
    birth_date = models.DateField()
    death_date = models.DateField()
