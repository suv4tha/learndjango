from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request,'work.html')
def signIn(request):
    return render(request,'sign.html')