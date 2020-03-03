from django.db import models
from midterm.utils.constants import Bullet, Food, Travel, Sport, Journal_type


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.PositiveIntegerField()
    genre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Journal(BookJournalBase):
    type = models.PositiveSmallIntegerField(choices=Journal_type, default=Bullet)
    publisher = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Journal"
        verbose_name_plural = "Journals"
