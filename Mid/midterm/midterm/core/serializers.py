from rest_framework import serializers
from .models import Book, Journal


def page_validator(pages):
    if not (1 <= pages <= 10000):
        raise ValueError("Invalid number of pages")


def type_validator(_type):
    if _type not in [1, 2, 3, 4]:
        raise ValueError("Invalid type")


def check_name(name):
    for n in name:
        if n == "$":
            raise ValueError("Not valid char")


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[check_name])
    num_pages = serializers.IntegerField(validators=[page_validator])

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'num_pages')


class JournalSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField(validators=[type_validator])

    class Meta:
        model = Journal
        fields = ('id', 'name', 'price', 'type')
