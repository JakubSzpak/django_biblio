from django.db import models
from django.contrib.auth.models import User
from shelf.models import BookItem

from django.utils.timezone import now
# Create your models here.
class Rental(models.Model):
    who = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    what = models.ForeignKey(BookItem, on_delete=models.DO_NOTHING,)
    when = models.DateTimeField(default=now())
    returned = models.DateTimeField(null=True, blank = True)

    def __str__(self):
        return '{who} {what} {when} {returned}'.format(who=self.who, what=self.what,
                                                       when=self.when, returned=self.returned)