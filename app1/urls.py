from django.urls import path
from app1.views import *
app_name='something1'

urlpatterns=[
    path('one/',one,name='one'),
    path('two/',two,name='two'),
]