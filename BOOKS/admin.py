from django.contrib import admin
from .models import  book , Genres, reviews
# Register your models here.
admin.site.register(book)
admin.site.register(Genres)
admin.site.register(reviews)
