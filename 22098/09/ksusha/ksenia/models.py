from django.db import models

class Buyers(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    born = models.DateField()

class Goods(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

class Buy(models.Model):
    buyers = models.ForeignKey(Buyers, on_delete=models.RESTRICT)
    goods = models.ForeignKey(Goods, on_delete=models.RESTRICT)
    data = models.DateField()
    


    
                            
                            
    
