from typing import Optional

from authors.models import Author


def get_author(author_id: str) -> Optional[Author]:
    try:
        return Author.objects.get(author_id=author_id)
    except Author.DoesNotExist:
        return None


def add_author(**kwargs: dict) -> Author:
    author_object = Author(
        author_id=kwargs.get('authorId'),
        name=kwargs.get("name"),
        phone_number=kwargs.get('phoneNumber'),
        birth_date=kwargs.get('birthDate'),
        death_date=kwargs.get('deathDate'))
    author_object.save()
    return author_object


def get_all_author_name():
    author_list = Author.objects.values_list('name', flat=True)
    return author_list
