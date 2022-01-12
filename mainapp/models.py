from django.db import models

# Create your models here.

class Talaba(models.Model):
    name = models.CharField(max_length=15, verbose_name="ismi")
    surname = models.CharField(max_length=15, verbose_name="familya")

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
