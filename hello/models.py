from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name





