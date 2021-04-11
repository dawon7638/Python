from django.db import models
from django.shortcuts import redirect
import re  


# Create your models here.

# Creating a new record
#     ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
# Reading existing records
#     Methods that return a single instance of a class
#         ClassName.objects.first() - gets the first record in the table
#         ClassName.objects.last() - gets the last record in the table
#         ClassName.objects.get(id=1) - gets the record in the table with the specified id
#             this method will throw an error unless only and exactly one record matches the query
#     Methods that return a list of instances of a class
#         ClassName.objects.all() - gets all the records in the table
#         ClassName.objects.filter(field1="value for field1", etc.) - gets any records matching the query provided
#         ClassName.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided
# Updating an existing record
#     c = ClassName.objects.get(id=1)
#     c.field_name = "some new value for field_name"
#     c.save()
# Deleting an existing record
#     c = ClassName.objects.get(id=1)
#     c.delete()
# Other helpful methods
#     Displaying records
#         ClassName.objects.get(id=1).__dict__ - shows all the values of a single record as a dictionary
#         ClassName.objects.all().values() - shows all the values of a QuerySet (i.e. multiple instances)
#     Ordering records
#         ClassName.objects.all().order_by("field_name") - orders by field provided, ascending
#         ClassName.objects.all().order_by("-field_name") - orders by field provided, descending

#     CharField
#         Any text that a user may enter. This has one required parameter, max_length, that is the maximum length of text that can be saved.
#     TextField
#         Like a CharField, but with no maximum length. Your user could copy the entire text of the Harry Potter series into the field and it would save in the database correctly.
#     IntegerField
#         Holds an integer value
#     FloatField
#         Holds a float value; this is good for numbers with potentially varying numbers of decimal places
#     DecimalField
#         This is a good field for a number with a fixed number of decimal places, like currency. There are 2 required parameters: max_digits refers to the total number of digits (before and after the decimal place), and decimal_places refers to how many decimal places.
#     BooleanField
#         Holds a boolean value
#     DateTimeField
#         Used for a combination of a specific date and time. This field can take two very useful optional parameters. Setting the auto_now_add argument to True adds the current date/time when an object is created. Setting auto_now=True automatically updates any time the object is modified.


# one to many:
#     class Author(models.Model):
#         name = models.CharField(max_length=255)
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     class Book(models.Model):
#         title = models.CharField(max_length=255)
#         author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     some_book.author	# returns the Author instance associated with this book
#     this_author = Author.objects.get(id=2)
#     books = Book.objects.filter(author=this_author)
#     this_author.books.all()



# Many to many:
#     class Book(models.Model):
#         title = models.CharField(max_length=255)
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     class Publisher(models.Model):
#         name = models.CharField(max_length=255)
#         books = models.ManyToManyField(Book, related_name="publishers")
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     add to each other
#         this_book = Book.objects.get(id=4)	# retrieve an instance of a book
#         this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
            
#         # 2 options that do the same thing:
#         this_publisher.books.add(this_book)		# add the book to this publisher's list of books
#         # OR
#         this_book.publishers.add(this_publisher)	# add the publisher to this book's list of publishers
#     remove relation:
#         this_book = Book.objects.get(id=4)	# retrieve an instance of a book
#         this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
            
#         # 2 options that do the same thing:
#         this_publisher.books.remove(this_book)		# remove the book from this publisher's list of books
#         # OR
#         this_book.publishers.remove(this_publisher)	# remove the publisher from this book's list of publishers
#     reverse lookup
#         this_publisher.books.all()	# get all the books this publisher is publishing
#         this_book.p ublishers.all()	# get all the publishers for this book



# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        errors = {}
        
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First Name must be at least 2 chars!"
            
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last Name must be at least 2 chars!"
            
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
class VehicleManager(models.Manager):
    def car_validator(self, postData):
        
        car_errors = {}
        
        if len(postData["year"]) < 4:
            car_errors["year"] = "Year must be at least 4 digits!"
            
        if len(postData["year"]) == None:
            car_errors["year"] = "Year must be provided!"
        
            
        if len(postData["make"]) < 3:
            car_errors["make"] = "Make be at least 3 chars!"

        if len(postData["make"]) == None:
            car_errors["make"] = "Make must be provided!"
            
        if len(postData["model"]) < 3:
            car_errors["model"] = "Model must be at least 3 chars!"
            
        if len(postData["model"]) == None:
            car_errors["model"] = "Model must be provided!"
            
        if len(postData["vin"]) == 17:
            car_errors["vin"] = "Vin must be 17 chars!"
            
        if len(postData["vin"]) == None:
            car_errors["vin"] = "Vin must be provided!"
            
        if len(postData["mileage"]) <= 100:
            car_errors["mileage"] = "Please provide actual mileage!"
            
        if len(postData["mileage"]) == None:
            car_errors["mileage"] = "Mileage must be provided!"
            
        if len(postData["note"]) < 5:
            car_errors["note"] = "Description must be at least 5 chars!"
            
        if len(postData["note"]) == None:
            car_errors["note"] = "Description must be provided!"
            

        return car_errors  
  
    
####################################################################



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    ###################################
    objects = UserManager()
    
    ###################################
    def __repr__(self):
        return f"User: {self.id} {self.first_name} {self.last_name} {self.email_address} {self.password}"
    
    
class Vehicle(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=45)
    model = models.CharField(max_length=100)
    vin = models.CharField(max_length=17)
    mileage = models.IntegerField()
    note = models.TextField()
    driver = models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    ###################################
    objects = VehicleManager()
    
    ###################################
    def __repr__(self):
        return f"User: {self.id} {self.year} {self.make} {self.model} {self.vin} {self.mileage} {self.note}"
