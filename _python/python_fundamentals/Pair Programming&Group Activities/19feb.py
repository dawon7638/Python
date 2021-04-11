rom django.db import models

#  Many-to-Many and One-to-many Exercises

# 1
# Create the models.py for an Events App

# Users can organize events, events can only have one organizer
# Users can attend many events, and events can have many users attending

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # whatever other fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    event_date = models.DateField()
    # whatever other fields / relationships
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Ninja Bonus! 2
# Create the models.py for a book lending app

# Users can post books to lend // books only have one lender
# Users can borrow books from other users // books only have one borrower

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # whatever other fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # whatever other fields/relationships
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)