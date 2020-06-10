from django.urls import path 
from . import views

urlpatterns = [
    path('',views.top, name='top'),
    path('index/All/',views.indexAll, name='index'),
    path('index/<str:cate>/',views.index),
    path('newone/',views.new, name='new'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('message/<int:pk>/',views.message,name="message"),
    path('signup/',views.signupfunc, name='signup' ),
    path('login/',views.loginfunc, name='login'),
    path('logout',views.logoutfunc, name='logout'),
]














