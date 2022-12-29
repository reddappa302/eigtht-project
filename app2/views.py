from django.shortcuts import render

# Create your views here.
def one1(request):
    d={'name':'red','favhero':'raviteja'}
    return render(request,'one1.html',d) 