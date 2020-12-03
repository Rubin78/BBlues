from math import ceil
from random import random

from django import template

register = template.Library()


@register.filter(is_safe=False)
def masonryKey(value, arg):
    """Return True if the value is divisible by the argument."""
    li = [1,0,1,1,0,0]
    return li[abs((value%6)-1)]


@register.filter(is_safe=False)
def masonryRandomKey(value, arg):
    """Return True if the value is divisible by the argument."""
    return round(random())