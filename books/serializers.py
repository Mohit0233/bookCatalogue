import json

from django.db import models
from django.db.models import QuerySet
from rest_framework import serializers

from authors.validators import validate_author_id
from books.validators import validate_category_id, validate_book_id
from django.core import serializers as django_serializers


class BookSerializer(serializers.Serializer):
    bookId = serializers.CharField(max_length=15, validators=[validate_book_id])
    title = serializers.CharField(max_length=50)
    authorId = serializers.CharField(max_length=15, validators=[validate_author_id])
    publisher = serializers.CharField(max_length=50)
    publishDate = serializers.DateField(input_formats=['%d-%m-%Y', '%d-%b-%Y'])
    categoryId = serializers.CharField(max_length=15, validators=[validate_category_id])
    price = serializers.FloatField()
    soldCount = serializers.IntegerField()


class CategorySerializer(serializers.Serializer):
    categoryId = serializers.CharField(max_length=15, validators=[validate_category_id])
    categoryName = serializers.CharField(max_length=20)


class PartialTitlePartialAuthorNameSerializer(serializers.Serializer):
    partialTitle = serializers.CharField(max_length=500, allow_blank=True)
    partialAuthorName = serializers.CharField(max_length=50, allow_blank=True)


class AuthorIdSerializer(serializers.Serializer):
    authorId = serializers.CharField(max_length=15, validators=[validate_author_id])


class CategoryIdSerializer(serializers.Serializer):
    categoryId = serializers.CharField(max_length=15, validators=[validate_category_id])


def serialize_python_object_to_json(ser_model: object) -> any:

    """
    takes the list, QuerySet of models.Model or models.Model directly\n
    serialize it\n
    and return in json format\n
    :param ser_model: list[models.Model], QuerySet[models.Model], models.Model
    :return: list[dict], dict
    """

    def model_serializer_separation(json_model):
        json_dic = {'id': json_model.get('pk')}
        json_dic.update(json_model.get('fields'))
        return json_dic

    if isinstance(ser_model, QuerySet) or isinstance(ser_model, list):
        json_model_list = json.loads(django_serializers.serialize('json', ser_model))
        return [model_serializer_separation(json_model) for json_model in json_model_list]

    if isinstance(ser_model, models.Model):
        json_model = json.loads(django_serializers.serialize('json', [ser_model, ]))[0]
        return model_serializer_separation(json_model)
