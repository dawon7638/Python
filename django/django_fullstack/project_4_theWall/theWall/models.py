from django.db import models
from django.shortcuts import redirect
import re  

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        
        errors = {}
        
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First Name must be at least 2 chars!"
            
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last Name must be at least 2 chars!"
            
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData["email_address"]):             
            errors["email_pattern"] = "Invalid email address!" 
            
        elif User.objects.filter(email_address = postData["email_address"]):
            errors["email_duplicate"] = "Email already exist!"
               
        if len(postData["email_address"]) == None:
            errors["email_length"] = "Email must be at least 2 chars!"
            
        if len(postData["password"]) == None:
            errors["password_length"] = "Password must be at least 8 chars!"
            
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be at least 8 chars!"
            
        if postData["confirmPassword"] != postData["password"] :
            errors["confirmPassword"] = "Password must match!"
            
            
        return errors
############################################################################  
  
    
####################################################################


###############################USER CLASS####################################
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    ##################################
    objects = UserManager()
    
    ###################################
    def __repr__(self):
        return f"User: {self.id} {self.first_name} {self.last_name} {self.email_address}"

###############################MESSAGE CLASS####################################
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="users_messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ###################################
    def __repr__(self):
        return f"Message: {self.id} {self.message}"
    
###############################COMMENT CLASS####################################  
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="users_comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="users_comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ###################################
    def __repr__(self):
        return f"Comment: {self.id} {self.comment}"
    