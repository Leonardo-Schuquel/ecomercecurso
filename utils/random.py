import string
from random import SystemRandom
from django.utils.text import slugify

def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits, k=5
    ))

def slugify_new(text, k):
    return slugify(text) + '-' + random_letters(k)