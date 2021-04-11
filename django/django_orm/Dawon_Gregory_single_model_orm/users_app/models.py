from django.db import models

# Create your models here.
    
class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    users.objects.create(first_name = "jim", last_name = "bob", email_address = "ihavenoteeth@aol.com", age = 40)
    users.objects.creat(first_name = "lucy", last_name = "lew", email_address = "chooseme@yahoo.com", age = 19)
    users.objects.create(first_name = "richard", last_name = "dix", email_address = "lolwhat@gmail.com", age = 39)
    
    
    users.objects.all()
    users.objects.last()
    users.objects.first()
    users_to_update = users.objects.get(id =3)
    users_to_update.last_name = "pancakes"
    users_to_update.save()
    users_to_delete = users.objects.get(id=2)
    users_to_delete.delete()
    users.objects.all().order_by("first_name")
    users.objects.all().order_by("-first_name")
    

    def __str__(self):
        return f"<users object: (self.first_name) ({self.id})>"
        