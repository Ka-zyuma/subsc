from django.urls import path 
from . import views
from .views import newone

urlpatterns = [
    path('index/',views.index, name='index'),
    path('newone/',newone.as_view(), name='newone'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('message/<int:pk>',views.message,name="message"),
]














