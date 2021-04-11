from django.db import models

# Create your models here.

    
class user (models.Model):
    userfirst = models.CharField(max_length=255)
    userlast = models.CharField(max_length=255)
    useremail = models.CharField(max_length=255)
    userage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"User: {id} {self.userfirst} {self.userlast}"

