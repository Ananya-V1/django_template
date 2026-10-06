from django.db import models

# Create your models here.
# models deal with the database
# models are always class-based and they inherit from Django's models class

# using SQLite database (lightweight, serverless database); django typcially autmaticall usues sqlite but you can change it

# SQLite: single file, with no server to install; used for simpler projects
# PostgreSQL: full database server; used for most real, deployed Django projects
# MySQL: full database server; used when company/host already uses MySQL

# typical pick is PostgreSQL

class MenuItem(models.Model):
    # define different attributes of the model
    # each attribute that is defined corresponds to a column in our database
    # if you don't define a primary key, Django will autmatically make an id columns and make that the primary key
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True) # store the current data automatically
    comments = models.CharField(max_length=1000)

