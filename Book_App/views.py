
from django.db.models import Q
from .models import Book
from django.shortcuts import render,redirect
from .forms import AuthorForm,Bookform
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
# def CreateBook(request):
#     books=Book.objects.all()
#     if request.method=="POST":

#         title=request.POST.get("title")
#         auther=request.POST.get("author")
#         price=request.POST.get("price")

#         book=Book(title=title,auther=auther,price=price)
#         book.save()

#     return render(request,"home.html",{'books':books})

def listbook(request):
    books=Book.objects.all()
    paginator=Paginator(books,5)
    page_number=request.GET.get("page")

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

      
    return render(request,'listbook.html',{'books':books,"page":page})
   

def details(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detail_view.html',{"book":book})


def update(request,book_id):
    # book=Book.objects.get(id=book_id)
    # if request. method=='POST':
    #     title=request.POST.get('title')
    #     price=request.POST.get('price')
    #     book.title=title
    #     book.price= price
    # book.save()
    #     return redirect('/')
    # return render (request,'update.html',{'books':book}) 



    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form= Bookform (request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Bookform(instance=book)
    return render(request,'update.html',{'form':form})   





# -----------------------------booststrap

def index(request):
    return render (request,'index.html')


        







        

def delete(request,book_id):
   book=Book.objects.get(id=book_id)
   if request.method=='POST':
       book.delete()
       return redirect('/')
   return render(request,'delete.html')


# form--------------------------------
def CreateBook(request):
    books=Book.objects.all()

    if request.method=='POST':
        form=Bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
   
    else:
        form= Bookform()      
       
    return render(request,'home.html',{'form':form,'books':books})
       
def Create_Author(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form . is_valid():
            form .save()
        return redirect('/')
    else:
        form= AuthorForm()  
    return render(request,'author.html',{'form':form})


def Search_Book(request):
    query=None
    books=None
    if 'q' in request .GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}
    return render (request,'search.html',context)    








# --- register-------------
def reg(request):
    if request.method=="POST":
        username=request.POST.get('username')
        firstname=request.POST.get('First_name')
        lastname=request.POST.get('Last_name')
        email=request.POST.get('Email')
        password=request.POST.get('Password')




        return render (request,'register.html')
    
  



