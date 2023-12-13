from django.db import models
from django.contrib.auth.models import User

# mallit

class Kurssi(models.Model):
    #kurssi, jonka tehtävä kyseessä
    kurssi = models.CharField(max_length=200)
    kayttaja = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Kurssit'

    def __str__(self):
        return self.kurssi


class Teht(models.Model):
    #kurssin tehtävänanto
    kurssi = models.ForeignKey(Kurssi, on_delete=models.CASCADE)
    teht = models.TextField()
    dedis = models.DateTimeField(null=True)
    valmis = models.BooleanField(null=True)


    class Meta:
        verbose_name_plural = 'Tehtavat'

    def __str__(self):
        return f"{self.teht[:50]}"