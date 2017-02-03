from django.db import models

# Create your models here.
class TA(models.Model):
    nr = models.IntegerField()
    data = models.DateField()    
    grupa = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "TA"
        verbose_name_plural = "TAs"

    def __str__(self):
        return str(self.nr)


class Etykieta(models.Model):
    nr = models.IntegerField()
    ta = models.ForeignKey(TA)
    pozycja = models.IntegerField()
    element = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Etykieta"
        verbose_name_plural = "Etykiety"

    def __str__(self):
        return str(self.nr)

    def elementy_ta(self, *args, **kwargs):
        return Etykieta.objects.filter(nr=self.nr)

class Zamowienia(models.Model):
    etykieta = models.ForeignKey(Etykieta)
    kod = models.IntegerField(default=0)
    data_rozpoczecia = models.DateTimeField(auto_now=True)
    data_zakonczenia = models.DateTimeField()

    class Meta:
        verbose_name = "Zamowienia"
        verbose_name_plural = "Zamowienia"

    def __str__(self):
        pass
    