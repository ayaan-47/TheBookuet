from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.shortcuts import reverse
from .validators import validate_file_size


class Genres(models.Model):
    name = models.CharField( max_length=50,default='Romance')  
    def __str__(self):
        return self.name
      

class book(models.Model):
    book_name = models.CharField(max_length=100,default="Enter Book Name")
    author_name = models.CharField(max_length=100,default="Enter Author Name")
    thumbnail = models.ImageField(blank = True)
    thumbnail_2 = models.ImageField(blank = True)
    book_pdf = models.FileField(blank=True,validators=[validate_file_size])
    synopsis = models.TextField(default="Enter Synopsis")
    review = models.TextField(default="Enter Review")
    Choices = (('fe','featured'),
    ('n','normal'))
    
    category = models.CharField( max_length=50,choices=Choices,default="n")  

    
    book_genre = models.ForeignKey(Genres,default=2,related_name='books',on_delete=models.CASCADE)
    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('homepage')


class reviews(models.Model):
    book_name = models.ForeignKey(book,default = 1, related_name='reviews',on_delete=models.CASCADE)
    review = models.CharField(default = "Yet to be reviewed" , max_length=500,blank=True)
    review_name = models.CharField(default = "Anonymous",max_length = 100, blank = True)

    def __str__(self):
        return self.review_name
   
 



    