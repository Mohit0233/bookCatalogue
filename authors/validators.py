from django.conf import settings

from authors.utility import regex_match_pattern


def validate_author_id(value):
    regex_match_pattern(settings.AUTHOR_ID_VALIDATION_REGEX, value)


def validate_name(value):
    regex_match_pattern(settings.NAME_VALIDATION_REGEX, value)

