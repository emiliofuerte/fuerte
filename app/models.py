from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    date_read = models.DateField(null=True)
    cover_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class Language(models.TextChoices):
    ENGLISH = 'en'
    FRENCH = 'fr'

class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    text = models.CharField(max_length=1024)
    language = models.CharField(choices=Language.choices, max_length=2, default=Language.ENGLISH)

    def __str__(self):
        return f'Review of {self.book}' 