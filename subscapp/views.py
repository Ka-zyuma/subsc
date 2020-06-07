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
# Create your views here.
def index(request,cate):
    if cate=='All':
        items = Subsc.objects.all()
    else:
        items = Subsc.objects.all().filter(category=cate)
    categories = Subsc.objects.values_list('category',flat='True').distinct()
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
    


class newone(CreateView):
    template_name='newone.html'
    model = Subsc
    fields = {'title','price','url','category','date'}
    success_url = reverse_lazy('index')
    
def message(request,pk):
    messages.info(request, 'Hello World')
    return redirect("message")

   


def delete(request, pk):
    Subsc.objects.filter(id=pk).delete()
    return redirect('index')


