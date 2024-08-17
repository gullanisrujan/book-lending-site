from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import User,ExpectedBooks
from book.models import Books
# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,'login.html',{'already':False,'wrong':False})
    elif request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            users=User.objects.get(uname=username,password=password)
        except:
            return  render(request,'login.html',{'already':False,'wrong':True})
        request.session['login']=True
        request.session['uid']=users.uid
        return redirect('../user/dashboard')
def register(request):
    if request.method=='POST':
        uname=request.POST["username"]
        password=request.POST["password"]
        uid=request.POST["userId"]
        uphone=request.POST["UPIno"]
        uimg = request.FILES["image"] 
        users=User.objects.all().filter(uid=uid)
        if users:
            return render(request,'register.html',{'already':True,'wrong':False})
        else:
            g=User(uname=uname,password=password,uid=uid,uphone=uphone,userImg=uimg)
            g.save()
            request.session['login']=True
            request.session['uid']=g.uid
            return redirect('../user/dashboard')
    else:
        return render(request,'register.html',{'already':False,'wrong':False})

def dashboard(request):
    login = request.session.get('login',False)
    if login:
        uid=request.session.get('uid',False)
        books=Books.objects.all().filter(buser=uid)
        user=User.objects.get(uid=uid)
        ebooks = ExpectedBooks.objects.all().filter(user=user)
        return render(request,'dashboard.html',{'user':user,'books':books,'ebooks':ebooks})
    else:
        return redirect('../user/login')
class EB:
    def __init__(self,book,exchange,ep):
        self.book=book
        self.exchange=exchange
        self.ep=ep
        self.fun()
    def fun(self):
        if len(self.ep) == 0:
            self.exchange=False
            self.ep=[0]
        
def search(request):
    login = request.session.get('login',False)
    if login and request.method=='POST':
        query= request.POST['query']
        uid=request.session.get('uid',False)
        books=Books.objects.all().filter(bname__icontains=str(query).strip())
        mybooks=set([i.bname for i in list(Books.objects.all().filter(buser=uid))])
        usersetlist=set()
        for book in books:
            if book.buser.uid == uid:
                continue
            usersetlist.add(book.buser)
        usersetlist=list(usersetlist)
        d={}
        for user in usersetlist:    
            d[user]=list(ExpectedBooks.objects.all().filter(user=user))
        for user in d:
            k=d[user]
            print(k)
            t=[]
            for b in k:
                if b.bname in mybooks:
                    t.append(b)
            d[user]=t
        res=[]
        print(books)
        for book in books:
            try:
                user=book.buser
                k=d[user] #expected books
                res.append(EB(book,True,k))
            except :
                continue
        if len(res)==0:
            return render(request,'resultsnofound.html')
        else:
            return render(request,'show.html',{'res':res,'me':uid})
    else:
        return redirect('../user/login')
    
def logout(request):
    request.session.pop('login')
    request.session.pop('uid')
    return redirect('../user/login')

 
    