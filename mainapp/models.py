from django.db import models

# Create your models here.

class DateTime(models.Model):
    sana = models.DateField(verbose_name="sana")

    def __str__(self):
        return str(self.sana)

    class Meta:
        verbose_name = "Sana"
        verbose_name_plural = "Sanalar"

class Talaba(models.Model):
    name = models.CharField(max_length=15, verbose_name="ismi")
    surname = models.CharField(max_length=15, verbose_name="familya")
    status = models.BooleanField(default=True)
    date = models.ForeignKey(DateTime, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"




