from django.shortcuts import render
from user.models import User,ExpectedBooks
from book.models import Books
from .models import Transactions
import datetime
import copy
# Create your views here.
def exchange(request):
    if request.method=="POST":
        uid=request.POST['uid']
        bookId=request.POST['bookId']
        mybookname=request.POST['mybook']
        print(uid,bookId,mybookname)
        me=User.objects.all().filter(uid=uid)
        book=Books.objects.all().filter(bookId=bookId)
        bookOner = book[0].buser
        t=Transactions(transactionId="TVITS"+str(datetime.datetime.now())[:11].replace(' ','').replace('-',''),
                       fromUser=me[0],
                       toUser=bookOner,
                       tamount=6,
                       exchangeType="exchange")
        t.save()
        t.transactionId=t.transactionId+str(t.tid)
        t.save()
        mybooks=Books.objects.all().filter(buser=uid).filter(bname=mybookname)[0]
        temp=book 
        book=copy.deepcopy(book[0])
        mybooks.delete()
        temp.delete()
    return render(request,'transaction.html',{'tid':t.transactionId,'type':'Exchange','book':book,'bookOner':bookOner,'me':me[0],'date':datetime.datetime.now(),'prize':0,'aprize':6})

def lend(request):
    if request.method == "POST":
        uid=request.POST['uid']
        bookId=request.POST['bookId']
        me=User.objects.all().filter(uid=uid)
        book=Books.objects.all().filter(bookId=bookId)
        bookOner = book[0].buser
        t=Transactions(transactionId="TVITS"+str(datetime.datetime.now())[:11].replace(' ','').replace('-',''),
                       fromUser=me[0],
                       toUser=bookOner,
                       tamount=book[0].plprize + 6,
                       exchangeType="lend")
        t.save()
        t.transactionId=t.transactionId+str(t.tid)
        t.save()
        book_copy = copy.deepcopy(book[0])
        book[0].delete()
    return render(request,'transaction.html',{'tid':t.transactionId,'type':'Lend','book':book_copy,'bookOner':bookOner,'me':me[0],'date':datetime.datetime.now(),'prize':book_copy.plprize,'aprize': book_copy.plprize + 6})

def buy(request):
    if request.method == "POST":
        uid=request.POST['uid']
        bookId=request.POST['bookId']
        me=User.objects.all().filter(uid=uid)
        book=Books.objects.all().filter(bookId=bookId)
        bookOner = book[0].buser
        t=Transactions(transactionId="TVITS"+str(datetime.datetime.now())[:11].replace(' ','').replace('-',''),
                       fromUser=me[0],
                       toUser=bookOner,
                       tamount=book[0].bprize+6,
                       exchangeType="buy")
        t.save()
        t.transactionId=t.transactionId+str(t.tid)
        t.save()
        book_copy = copy.deepcopy(book[0])
        book[0].delete()
    return render(request,'transaction.html',{'tid':t.transactionId,'type':'Buy','book':book_copy,'bookOner':bookOner,'me':me[0],'date':datetime.datetime.now(),'prize': book_copy.bprize,'aprize':book_copy.bprize+6})