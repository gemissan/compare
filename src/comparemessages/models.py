from django.db import models

from comparemessages.managers import MessageManager


class Message(models.Model):
    
    name = models.CharField(max_length=20, primary_key=True)
    message = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name']
        
    objects = MessageManager()
    
    def natural_key(self):
        
        return (self.name,)