from django.db import models

# Create your models here.

class Subjects(models.Model): #Category
    """This model works as category for each course"""
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.title


