from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class City(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # Foreign key to City

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=128)
    courses = models.ManyToManyField(Course)  # Many-to-many relationship

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username  # Fixed to return a string representation of the user

class Musician(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Musician, through="Membership")
    slug = models.SlugField(max_length=128, blank=True, unique=True, editable=False, default='') 

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.name.lower() == "winners":
            raise ValidationError("Group name cannot be 'winners'.")

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Membership(models.Model):
    person = models.ForeignKey(Musician, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now=True)
    invite_reason = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.person.name} - {self.group.name}"  
    
# multi table inheritance
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.name

class Supplier(Place):
    contact_number = models.CharField(max_length=15, blank=True)
    customers = models.ManyToManyField(Place, related_name='providers')

    def __str__(self):
        return f"Supplier: {self.name}"
    def get_customers(self):
        return self.customers.all()

# proxy model
class PersonProxy(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class MyPersonProxy(PersonProxy):
    class Meta:
        proxy = True

    def do_something(self):
        # Custom method
        pass
