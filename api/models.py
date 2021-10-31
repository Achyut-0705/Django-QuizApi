from django.db import models

# Create your models here.
class Question(models.Model):
    statement = models.CharField(max_length=256)
    option_a = models.CharField(max_length=64)
    option_b = models.CharField(max_length=64)
    option_c = models.CharField(max_length=64)
    option_d = models.CharField(max_length=64)
    correct = models.CharField(max_length=1)
    link = models.CharField(max_length=128)

    def __str__(self):
        return 'Question: ' + str(self.id)