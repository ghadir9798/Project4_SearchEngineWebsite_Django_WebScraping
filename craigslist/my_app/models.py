from django.db import models
from django.utils import timezone

# Create your models here.
class Search(models.Model):
    search_content = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{}'.format(self.search_content)

    class Meta:
        verbose_name_plural = 'searches'