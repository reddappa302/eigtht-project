from django.shortcuts import render

# Create your views here.
def one(request):
    d={'name':'green','favhero':'prabhas'}
    return render(request,'one.html',context=d)

def two(request):
    d={'name':'green','favcolor':'black'}
    return render(request,'two.html',context=d)


