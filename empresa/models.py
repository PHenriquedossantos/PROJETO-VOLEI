from django.db import models

class Company(models.Model):
    """Refere-se ao local ex: Kartney"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Place(models.Model):
    """refere-se a quadra ou campo do local"""
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Payment(models.Model):
    """Pagamento"""
    PAYMENT_TYPES = (
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
        ('outro', 'Outro'),
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPES)
    
    def __str__(self):
        return self.payment_type

class Scheduling(models.Model):
    date = models.DateField()
    entry_time = models.TimeField()
    exit_time = models.TimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

#127.0.0.0.8000/customer/id_customer/horario
#CUSTOME.NOME
#COMPANY.NAME
#PLACE.NAME

