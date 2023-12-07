from django.db import models

# Create your models here.

class Kurssi(models.Model):
    #kurssi, jonka tehtävä kyseessä
    kurssi = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Kurssit'

    def __str__(self):
        return self.kurssi


class Teht(models.Model):
    #kurssin tehtävänannon nimi
    kurssi = models.ForeignKey(Kurssi, on_delete=models.CASCADE)
    teht = models.TextField()

    class Meta:
        verbose_name_plural = 'Tehtavat'

    def __str__(self):
        return f"{self.text[:50]}"