import json

from django.db import models


class CommonInfoModel(models.Model):

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    class Meta:
        abstract = True


class Author(CommonInfoModel):
    author_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=True)
    birth_date = models.DateField()
    death_date = models.DateField(null=True)
