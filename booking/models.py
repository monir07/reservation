from django.db import models


class Train(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
