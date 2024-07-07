from django.urls import path
from myproject import views

app_name = "myproject"

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name ='about'),
]