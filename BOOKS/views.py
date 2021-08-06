# from .models import mypeople
# from .forms import pform
# from typing_extensions import Required
from typing import List
from django.shortcuts import render,redirect
from django.urls.base import reverse
from django.views.generic import ListView,DeleteView,UpdateView,DetailView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy 
from .models import book,Genres,reviews
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.db.models import Q, fields
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import ReviewForm
# Create your views here.

def Book_Index(request):
  
    # bshelf = book.objects.filter(Q(category__in =['fe']) | Q(sub_category__in =['r']) )
    # bshelf = book.objects.filter(Q(category__in =['fe']))
    bshelf = book.objects.filter(category = 'fe')
    return render (request,"index.html",{'bshelf':bshelf})

# def Recent_Post(request):
#     questions = Genres.objects.annotate(total_books = Count('books')).order_by('id')
#     return render(request, "base.html",{'questions':questions})
   
 
def all_questions(request):
    questions = Genres.objects.annotate(total_books=Count('books')).order_by('id')

    answers = Genres.objects.all()
    return render(request, 'categories_list.html', {'questions':questions},{'answers':answers})


def Book_List(request, pk):
        gen = Genres.objects.annotate(total_books=Count('books')).filter(id = pk)
        shelfed = book.objects.filter(book_genre = pk)

        return render(request,"all_books.html",{'shelfed':shelfed},{'gen':gen})
# def Book_List_two(request,pk):
#         shelf = Genres.objects.annotate(total_books=Count('book')).filter(id = pk)
#         shelf = book.objects.filter(book_genre = pk)
#         return render(request,"all_books.html",{'shelf':shelf})


    
    


# Older method containing Strings as passed 
# def Book_Details(request, cat):
#    shelf = book.objects.filter(sub_category=cat)
#    counting = shelf.count()
#    return render (request,"synopsis.html",{'cat':cat, 'shelf':shelf ,'counting':counting })
def Book_Details(request, pk):
        gen = Genres.objects.annotate(total_books=Count('books')).filter(id = pk)
        shelfed = book.objects.filter(book_genre = pk)
        return render(request,"synopsis.html",{'shelfed':shelfed},{'gen':gen})



def createreview(request):
    if request.method == 'GET':
        return render(request, 'review.html', {'form':ReviewForm()})
    else:
        try:
            form = ReviewForm(request.POST)
            newtodo = form.save(commit=False)
            
            newtodo.save()
            return redirect('homepage')
        except ValueError:
            return render(request, 'review.html', {'form':ReviewForm(), 'error':'Bad data passed in. Try again.'})

def Search_Page(request):
    return render (request, "search_page.html")

def Search_All_Books(request):

    search = request.POST['search']
    result = book.objects.filter(book_name__icontains= search)
    return render (request ,'search_all_books.html',{'result':result},{'search':search})


def Contact(request):
    name = request.POST.get('name')
    return render (request,'contact.html',{'name':name})

@method_decorator(login_required, name='dispatch') 
class Book_Edit_Delete(DetailView):
    model = book
    template_name = "edit_delete.html"
    context_object_name = 'shelf'
@method_decorator(login_required, name='dispatch') 
class Book_Edit_List(ListView):
    model = book
    template_name = "book_edit_list.html"
    context_object_name = 'shelf'
    ordering =['-book_genre']


class Book_List_all(ListView):
    model = book
    template_name = "all_books.html"
    context_object_name = 'shelfed'
    ordering = ['category']



class Book_Details_all(ListView):
    ordering = ['book_name']
    paginate_by = 3
    model = book
    template_name = "synopsis.html"
    context_object_name = 'shelfed'
   
class Single_Book_Details(DetailView):
    model = book
    template_name = "single_book.html"
    context_object_name = 'shelf'

class Review_Form(FormView):
    template_name = 'single_book.html'
    form_class = ReviewForm
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.working()
        return super().form_valid(form) 


@method_decorator(login_required, name='dispatch') 
class Book_Edit(UpdateView):
    model = book
    template_name ="edit.html"
    fields = ['book_name','author_name','thumbnail','book_pdf', 'synopsis', 'review','thumbnail_2','book_genre','category']
    context_object_name = 'shelf'

@method_decorator(login_required, name='dispatch') 
class Book_Delete(DeleteView):
    model = book
    template_name = "delete.html"
    context_object_name = 'shelf'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required, name='dispatch') 
class Book_Create(CreateView):
    model = book
    template_name = "create.html"
    fields = ['book_name','author_name','thumbnail','book_pdf', 'synopsis', 'review','thumbnail_2','book_genre','category']
    success_url = reverse_lazy('homepage')






def loginuser(request):
     if request.method=='GET':
        return render(request,'loginuser.html',{'form':AuthenticationForm})
     else:
         user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
         if user is None:
             return render(request,'loginuser.html',{'form':AuthenticationForm,'error':'Either username does not exist or Password doesnot match the user name'})
         else:
             login(request,user)
             return redirect('homepage') 
    
def signupuser(request):
    if request.method=='GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('homepage')

          
          
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm,'error':'Please Choose Another UserName!'})
        else:
                  return render(request,'signup.html',{'form':UserCreationForm,'error':'Please Enter the PASSWORD AS MENTIONED!'})
@login_required
def logout(request):
    auth.logout(request)
    return redirect('homepage')