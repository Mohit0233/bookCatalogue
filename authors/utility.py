import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def regex_match_pattern(regex: str, value: str):
    """
    regex patter.fullmatch() utility
    :param regex: regex pattern string
    :param value: value to be matched with regex
    """
    pattern = re.compile(regex)
    if not pattern.fullmatch(value):
        raise ValidationError(f'{value} does not match {regex} validation')


def json_default(value):
    """
    utility function for change json default while doing json loads
    :param value:
    :return:
    """
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__
