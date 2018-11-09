from django.db import models




# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name,
                                                 last_name=self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title


class BookEdition(models.Model):
    # "Wydane książki"
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, )
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, )
    date = models.DateField()
    isbn = models.CharField(max_length=17, blank= True)

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book,
                                                       publisher=self.publisher)


COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard')
    # (wartosc przechowywana w bazie, wartosc wyświetlana)
)


class BookItem(models.Model):
    # "KOnkretny egzembplarz"
    edition = models.ForeignKey(BookEdition,on_delete = models.DO_NOTHING,)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __str__(self):
        return "{edition},{cover}".format(edition=self.edition,
                                          cover=self.get_cover_type_display())
