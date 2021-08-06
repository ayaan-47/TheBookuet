from django.urls import path
from .import views


urlpatterns = [
    path('',views.Book_Index,name="homepage"),
    # path('',views.Recent_Post , name= 'base'),

    path('categories_list',views.all_questions,name="categories_list"),

    path('contact',views.Contact,name = 'contact'),

    path('synopsis',views.Book_Details_all.as_view(),name="synopsis"),
    path('genre_synopsis/<int:pk>/',views.Book_Details,name="genre_synopsis"),

    
    path('all_books',views.Book_List_all.as_view(),name="all_books"),
    path('genre/<int:pk>/',views.Book_List,name="genre"),
 
    path('single_book/<int:pk>/',views.Single_Book_Details.as_view(),name="single_book"),
    # path('single_book/<int:pk>/',views.Single_Book_review,name="single_book"),


    # path('genre/<int:pk>',views.Book_List_two,name='genres'),


    path('review',views.createreview , name = 'review'),
    path('search_page',views.Search_Page,name='search_page'),
    path('search_all_books',views.Search_All_Books,name='search_all_books'),



    path('book_edit/<int:pk>',views.Book_Edit.as_view(),name="book_edit"),
    path('book_edit_list',views.Book_Edit_List.as_view(),name="book_edit_list"),
    path('book_edit_delete/<int:pk>',views.Book_Edit_Delete.as_view(),name='book_edit_delete'),
    path('book_delete/<int:pk>',views.Book_Delete.as_view(),name="book_delete"),


    path('book_create',views.Book_Create.as_view(),name="create"),
    # path('book_detail/<int:pk>',views.Book_Details.as_view(),name="details"),
    path('login',views.loginuser,name = 'login'),
    path('logout',views.logout,name='logoutuser'),
    path('signup',views.signupuser,name='signup'),
    
]


