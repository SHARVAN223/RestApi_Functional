from django.db import models

class Student1(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Age = models.IntegerField()
    Contact = models.CharField(max_length=15)


    
