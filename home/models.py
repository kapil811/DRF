from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length= 100)
    age = models.IntegerField(default=18)
    father = models.CharField(max_length=100)



class category(models.Model):
    cat_name = models.CharField(max_length= 100)


class book(models.Model):
    cat_name = models.ForeignKey(category, on_delete= models.CASCADE)
    book_title = models.CharField(max_length= 100)