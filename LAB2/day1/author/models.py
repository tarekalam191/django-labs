
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def get_all_author(cls):
        return [(author.id, author.name) for author in cls.objects.all()]

    @classmethod
    def get_author_by_id(cls, author_id):
        return cls.objects.get(id=author_id)


    def __str__(self):
        return self.name
        # return self.id