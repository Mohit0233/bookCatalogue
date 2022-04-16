import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def regex_match_pattern(regex, value):
    pattern = re.compile(regex)
    if not pattern.fullmatch(value):
        raise ValidationError(f'{value} does not match {regex} validation')


def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__
