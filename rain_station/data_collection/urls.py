from re import A
from django.urls import path
from . import views


urlpatterns = [
    path('',views.apioverview, name='api-overview'),
    path('data_list/',views.data_list,name='data_list'),
    path('data_creat/',views.data_creat,name='data_creat')
]