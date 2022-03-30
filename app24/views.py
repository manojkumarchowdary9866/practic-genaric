from django.shortcuts import render

# Create your views here.
def p(request):
    return render(request,'p.html')