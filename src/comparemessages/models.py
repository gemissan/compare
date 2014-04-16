from django.db import models

from comparemessages.managers import MessageManager


class Message(models.Model):
    
    INFO = "IF"
    WARNING = "WR"
    ERROR = "ER"
    
    TYPE_CHOICES = (
        (INFO, "Info"),
        (WARNING, "Warning"),
        (ERROR, "Error"),
    )
    
    name = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    fades = models.BooleanField(default=False)
    message = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name']
        
    objects = MessageManager()
    
    def natural_key(self):
        
        return (self.name,)