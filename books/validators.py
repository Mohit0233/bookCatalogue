from django.conf import settings

from authors.utility import regex_match_pattern


def validate_book_id(value):
    regex_match_pattern(settings.BOOK_ID_VALIDATION_REGEX, value)


def validate_category_id(value):
    regex_match_pattern(settings.CATEGORY_ID_VALIDATION_REGEX, value)
