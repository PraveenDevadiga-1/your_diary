from django.db import models
# Create your models here.
class Diary_Page(models.Model):
    name=models.CharField(max_length=256)
    date=models.DateField()
    title=models.CharField(max_length=10)
    note=models.CharField(max_length=5000)

    def __str__(self):
        return self.name
