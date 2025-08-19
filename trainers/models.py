
from django.db import models 

class addNewTrainer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, default='Math')
    age = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="trainer_images/",) 
    
    def __str__(self):
        return (f"{self.name}-{self.subject}")