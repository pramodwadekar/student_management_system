from django.db import models

class student(models.Model):
    Fullname = models.CharField(max_length=50)
    DOB = models.DateField()
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()
    Gender = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=50)
    Qualification =models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.Fullname