from django.shortcuts import render,HttpResponse,redirect
from .forms import HeroForm,HeroApplication
# Create your views here.
def index(request):
    return render(request,'cwApp/index.html',)
def application(request):
    apply=HeroForm(request.POST or None)
    context={
        'form':apply,
    }
    if request.method == 'POST':
        if apply.is_valid():
            apply.save()
            return redirect('conformation')

        else:
            apply=HeroForm(request.POST)
            context={
                'form':apply,
            }
            return render(request,'cwApp/application.html',context)
    return render(request,'cwApp/application.html',context)

def conformation(request):
    return render(request,'cwApp/conformation.html',)