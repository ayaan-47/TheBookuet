from django.forms import ModelForm, fields
from .models import reviews

class ReviewForm(ModelForm):
    class Meta:
        model = reviews
        fields = ['book_name' , 'review','review_name']
