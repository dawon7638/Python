from django.db import models
from django.shortcuts import redirect
import re  

# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, postData):
        
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
class BookManager(models.Manager):
    def book_validator(self, postData):
        
        book_errors = {}
        
        if len(postData["title"]) == None:
            errors["first_name"] = "Title is required!"
            
        if len(postData["desc"]) < 5:
            errors["last_name"] = "Description must be at least 5 chars!"
            
            
        return book_errors 
  
    
####################################################################





class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ##################################
    objects = UserManager()
    
    def __repr__(self):
        return f"User: ({self.id}) {self.first_name} {self.last_name} {self.email_address} {self.password}"
    ###################################
    
    
class Book(models.Model): 
    title = models.CharField(max_length=80)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ###################################
    objects = BookManager()
    
    def __repr__(self):
        return f"Book: ({self.id}) {self.title} {self.desc} {self.user}"
    ###################################
    
    

    
