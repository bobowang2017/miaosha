# coding: utf-8
from enum import Enum, unique


@unique
class RedisPrefix(Enum):
    USER = 'user'
    ORDER = 'order'
    TOKEN = 'token'
    GOOD = 'good'

