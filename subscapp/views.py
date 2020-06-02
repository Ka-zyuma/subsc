from django.shortcuts import render,redirect
from .models import Subsc
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Sum
from datetime import date
import random
from django.contrib import messages
# Create your views here.
def index(request):
    items = Subsc.objects.all().filter(category='Movie')
    s = 0
    prices = Subsc.objects.all()
    for price in prices:
        s += price.price
    for day in items:
        x1 = date.today() - day.date
        day.period = x1.days
        day.save()
    recs = random.choice(("https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.scdn.co%2Fi%2F_global%2Fopen-graph-default.png&imgrefurl=https%3A%2F%2Fwww.spotify.com%2Fjp%2F&tbnid=EJxAr9DvxZhERM&vet=12ahUKEwi-t8yjzdvpAhWFy4sBHSPqC9IQMygBegUIARDrAQ..i&docid=0aq1zU_Mlei_QM&w=1200&h=630&q=spotify&ved=2ahUKEwi-t8yjzdvpAhWFy4sBHSPqC9IQMygBegUIARDrAQ","https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fy%2Fyui-papa1214%2F20200210%2F20200210192300.jpg&imgrefurl=https%3A%2F%2Fwww.yui-papa.com%2Fentry%2F2020%2F02%2F10%2F191018&tbnid=_7netLRSSoHe3M&vet=12ahUKEwjCodG6zdvpAhXDAqYKHfOoBk4QMygCegUIARDsAQ..i&docid=6juITzpCEdxI6M&w=719&h=295&q=youtube%20premium&ved=2ahUKEwjCodG6zdvpAhXDAqYKHfOoBk4QMygCegUIARDsAQ"))

    return render(request, 'index.html',{'items':items,'prices':s,'recs':recs})
    


class newone(CreateView):
    template_name='newone.html'
    model = Subsc
    fields = {'title','price','url','category'}
    success_url = reverse_lazy('index')
    
def message(request,pk):
    messages.info(request, 'Hello World')
    return redirect("message")

   


def delete(request, pk):
    Subsc.objects.filter(id=pk).delete()
    return redirect('index')


