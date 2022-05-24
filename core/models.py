from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)


class Journal(BookJournalBase):
    theme = models.TextChoices('theme', 'BULLET FOOD TRAVEL SPORT')
    publisher = models.CharField(max_length=100)
