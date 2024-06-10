from django.db import models

class CADExchangeRate(models.Model):
    currency = models.CharField(max_length=3)  
    date = models.DateField()  
    rate = models.DecimalField(max_digits=10, decimal_places=6)  

    def __str__(self):
        return f"1 CAD to {self.currency} on {self.date}: {self.rate}"

class EURExchangeRate(models.Model):
    currency = models.CharField(max_length=3)  
    date = models.DateField()  
    rate = models.DecimalField(max_digits=10, decimal_places=6)  

    def __str__(self):
        return f"1 EUR to {self.currency} on {self.date}: {self.rate}"

class USDExchangeRate(models.Model):
    currency = models.CharField(max_length=3)  
    date = models.DateField()  
    rate = models.DecimalField(max_digits=10, decimal_places=6) 

    def __str__(self):
        return f"1 USD to {self.currency} on {self.date}: {self.rate}"
