
from django.urls import path
from . import views
urlpatterns = [
 
    path('create',views.CreateBook,name='CreateBook'),
    path('',views.listbook,name='listbook'),
    path('detail/<int:book_id>/',views.details,name='details'),
    path('update/<int:book_id>/',views.update,name='update'),
    path('delete/<int:book_id>/',views.delete,name='delete'),
    path('author',views.Create_Author,name='Author'),
    path('index',views.index),
    path('search/',views.Search_Book,name='search')
]