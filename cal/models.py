from django.db import models

# Create your models here.
class Numbers(models.Model):
    date1 = models.DateField(verbose_name = "Published Date1",null=True,blank=True)
    date2 = models.DateField(verbose_name = "Published Date2",null=True,blank=True)


    def __str__(self):
        return self.date1,self.date2


    def compare(self):
        return self.date1 > self.date2