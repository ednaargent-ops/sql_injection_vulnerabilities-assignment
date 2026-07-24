from django.db import models

# Create your models here.
class Part(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'parts'

    def __str__(self):
        return self.name