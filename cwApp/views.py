from django.shortcuts import render,HttpResponse,redirect
from .forms import HeroForm,HeroApplication
# Create your views here.
def index(request):  #sends user to welcome page
    return render(request,'cwApp/index.html',)
def application(request): #application
    apply=HeroForm(request.POST or None)
    context={
        'form':apply,
    }
    if request.method == 'POST':   #if this is a post method
        if apply.is_valid():  #if the application is valid
            apply.save()
            return redirect('conformation')

        else:   #if there are errors
            apply=HeroForm(request.POST)
            context={
                'form':apply,
                'errors':apply.errors
            }
            return render(request,'cwApp/application.html',context) #return back to application will filled our information
    return render(request,'cwApp/application.html',context)

def conformation(request): #sends user to conformation page
    return render(request,'cwApp/conformation.html',)