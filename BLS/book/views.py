from django.shortcuts import redirect, render
from .models import Books
from user.models import User,ExpectedBooks
# Create your views here.
def add(request):
    login = request.session.get('login',False)
    if login:
        if request.method == "POST":
            uid=request.session.get('uid',False)
            bname= request.POST['bname']
            bdesc=  request.POST['bdesc']
            buser=  User.objects.get(uid=uid)
            bprize= request.POST['bprize']
            plprize= request.POST['blprize']
            book=Books(bname=str(bname).strip(),bdesc=bdesc,buser=buser,bprize=bprize,plprize=plprize)
            book.save()
            return redirect('../user/dashboard')
        else:
            return render(request,'add.html')

def delete(request):
    if request.method == "POST":
        bid= request.POST['bookid']
        print(bid)
        Books.objects.all().filter(bookId=bid).delete()
        return redirect('../user/dashboard')
    
# Create your views here.
def eadd(request):
    login = request.session.get('login',False)
    if login:
        if request.method == "POST":
            uid=request.session.get('uid',False)
            bname= request.POST['bname']
            buser= User.objects.get(uid=uid)
            book=ExpectedBooks(bname=str(bname).strip(),user=buser)
            book.save()
            return redirect('../user/dashboard')
        else:
            return render(request,'eadd.html')

def edelete(request):
    if request.method == "POST":
        bid= request.POST['bookid']
        ExpectedBooks.objects.all().filter(bookId=bid).delete()
        return redirect('../user/dashboard')