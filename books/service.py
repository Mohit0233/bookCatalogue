from typing import Optional, Union, Tuple

from django.db.models import Q
from rest_framework.response import Response as RestResponse

from authors.service import get_author
from books.models import Book, Category


def get_book(book_id: str) -> Optional[Book]:
    try:
        return Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        return None


def get_category(category_id: str) -> Optional[Category]:
    try:
        return Category.objects.get(category_id=category_id)
    except Category.DoesNotExist:
        return None


def add_book_to_catalog(**kwargs: dict) -> tuple[Book, bool]:

    book_object = get_book(str(kwargs.get('bookId')))
    if book_object:
        return book_object, False

    # checks for valid author
    author_object = get_author(str(kwargs.get('authorId')))
    if not author_object:
        raise ValueError("Author not found")

    # checks for category author
    category_object = get_category(str(kwargs.get('categoryId')))
    if not category_object:
        raise ValueError("Category not found")

    book_object = Book(
        kwargs.get('bookId'),
        kwargs.get('title'),
        kwargs.get('authorId'),
        kwargs.get('publisher'),
        kwargs.get('publishDate'),
        kwargs.get('categoryId'),
        kwargs.get('price'),
        kwargs.get('soldCount'),
    )

    book_object.save()
    return book_object, True


def get_or_add_category(**kwargs: dict) -> tuple[Category, bool]:
    category_object = Category.objects.get(kwargs.get('categoryId'))
    if category_object:
        return category_object, False
    category_object = Category(kwargs.get('categoryId'), kwargs.get('categoryName'))
    category_object.save()
    return category_object, True


def get_list_of_categories() -> list[str]:
    return Category.objects.values_list('category_name', flat=True)


def get_most_books_sold_by_author(author_id: str) -> Optional[Book]:
    try:
        return Book.objects.filter(author__author_id=author_id).order_by('-sold_count')[0]
    except IndexError:
        return None


def get_most_books_sold_by_category(category_id: str) -> Optional[Book]:
    try:
        return Book.objects.filter(category__category_id=category_id).order_by('-sold_count')[0]
    except IndexError:
        return None


def search_book(partial_title: str = None, partial_author_name: str = None) -> list[Book]:
    book_object_list = Book.objects.filter(
        Q(title__contains=partial_title) | Q(author__name__contains=partial_author_name))
    return book_object_list


def get_books_by_author(author_id: str) -> list[str]:
    return [next(iter(book_id_dict.values())) for book_id_dict in
            Book.objects.filter(author__author_id=author_id).values('book_id')]


def get_or_add_book(**kwargs: dict) -> tuple[str, int]:

    try:
        book_object, is_created = add_book_to_catalog(**kwargs)

        if book_object:
            if is_created:
                return "Success", 200
            else:
                return "Book is already Present", 200
        else:
            return "Failed to add book to catalog", 400

    except ValueError as e:

        return str(e), 400
