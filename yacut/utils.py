from random import choices
from re import match
from string import ascii_letters, digits

from .models import URLMap


def get_unique_short_id(length=6):
    """Генерирует уникальный короткий идентификатор."""
    characters = ascii_letters + digits
    while True:
        short_id = ''.join(choices(characters, k=length))
        if URLMap.query.filter_by(short=short_id).first() is None:
            return short_id


def check_short(short):
    """Проверяет, соответствует ли строка формату короткой ссылки."""
    pattern = r'^[A-Za-z0-9]{1,16}$'
    return bool(match(pattern, short))
