from django.shortcuts import render,redirect
from .models import Subsc
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Sum
from datetime import date
import datetime
import random
from django.contrib import messages
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def top(request):
    #requet.user.is_anonymousでloginしているかどうかチェック
    if request.user.is_anonymous:
        return render(request, 'top.html')
        
    else:
        return redirect('index')
# この下のやつがあればloginしてない人をはじけられる
@login_required
def index(request,cate):
    if cate=='All':
        items = Subsc.objects.all().filter(username=request.user)
        #requetにloginしているuserの情報がある
    else:
        items = Subsc.objects.all().filter(category=cate,username=request.user)
    categories = Subsc.objects.values_list('category',flat='True').filter(username=request.user).distinct()
    #vaules_listで特定のfieldsだけを取得
    #distinct()で重複を削除

    s = 0
    prices = items
    for price in prices:
        s += price.price
    for item in items:
        x1 = date.today() - item.date
        item.period = x1.days
        x2 = item.date + relativedelta(months=1) - date.today()
        #日数の計算はdatetime、timedelta,relativedeltなどで行う
        item.dateleft = x2.days
        item.save()
    
    
    recs = random.choice(("https://www.phileweb.com/news/ogp/d-av/456/45657.jpg","https://parentzone.org.uk/sites/default/files/580b57fcd9996e24bc43c529.png"))

    return render(request, 'index.html',{'items':items,'prices':s,'recs':recs,'categories':categories})
@login_required
def indexAll(request):  
    items = Subsc.objects.all().filter(username=request.user)
    categories = Subsc.objects.values_list('category',flat='True').filter(username=request.user).distinct()
    s = 0
    prices = items
    for price in prices:
        s += price.price
    for item in items:
        x1 = date.today() - item.date
        item.period = x1.days
        x2 = item.date + relativedelta(months=1) - date.today()
        #日数の計算はdatetime、timedelta,relativedeltなどで行う
        item.dateleft = x2.days
        item.save()
    
    
    recs = random.choice(("https://www.phileweb.com/news/ogp/d-av/456/45657.jpg","https://parentzone.org.uk/sites/default/files/580b57fcd9996e24bc43c529.png"))

    return render(request, 'index.html',{'items':items,'prices':s,'recs':recs,'categories':categories})
    
@login_required
def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        price = request.POST['price']
        category = request.POST['category']
        new = Subsc(title=title ,url=url ,price=price ,username=request.user, category=category)
        #model名(field=中身)にして、saveで保存
        new.save()
        return redirect('index')
    else:
        return render(request,'newone.html')

    
def message(request,pk):
    messages.info(request, 'Hello World')
    return redirect("message")

   

@login_required
def delete(request, pk):
    Subsc.objects.filter(id=pk).delete()
    return redirect('index')

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error':'このユーザー名は既に使われています'})
        except:
            user = User.objects.create_user(username, '',password)
        #authenticateしなくても、createしただけでloginできる
        if user is not None:
            login(request, user)
            return redirect('../index/All/')
        else:
            return redirect('signup')
        
        
    else:    
        return render(request ,'signup.html')
def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../index/All/')
        else:
            return redirect('login')
        
    else:    
        return render(request ,'login.html')
@login_required       
def logoutfunc(request):
    logout(request)
    return redirect('top')