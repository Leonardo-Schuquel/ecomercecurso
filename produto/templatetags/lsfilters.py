from django.template import Library
from utils import help

register = Library()

@register.filter
def format_price(val):
    return help.format_price(val)