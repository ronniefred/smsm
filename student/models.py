from django.db import models

# Create your models here.

class registration(models.Model): 
    FirstName = models.CharField(max_length = 15)
    LastName = models.CharField(max_length = 20)
    Course = models.CharField(max_length = 20)
    Email = models.EmailField(max_length = 30)
    Phone_number = models.PositiveIntegerField()
    State_of_origin = models.CharField(max_length = 20)
    Date_of_birth = models.DateField()
    Registration_date = models.DateField()
    Starting_date = models.DateField()
    Ending_date = models.DateField()
    Address = models.CharField(max_length = 20)
    def __str__(self):
        return  self.LastName
    
    