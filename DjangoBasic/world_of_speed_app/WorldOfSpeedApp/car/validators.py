from django.core.exceptions import ValidationError


def validate_year(year):
    MIN_YEAR = 1999
    MAX_YEAR = 2030

    if year < MIN_YEAR or year > MAX_YEAR:
        raise ValidationError('Year must be between 1999 and 2030!')