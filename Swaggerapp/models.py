from django.db import models

class Emp(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    esal = models.DecimalField(max_digits=10,decimal_places=2)
    eddr = models.CharField(max_length=100)

    def __str__(self):
        return self.ename