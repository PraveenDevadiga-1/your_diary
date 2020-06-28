from django.shortcuts import render
from your_diary_app.forms import UserForm
from your_diary_app.forms import Diary_Page_Form
from your_diary_app.models import Diary_Page
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'your_diary_app/index.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required()
def diary(request):
    return render(request,'your_diary_app/diary.html')

def register(request):
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=UserForm()
    return  render(request,'your_diary_app/register.html',{'registered':registered,'user_form':user_form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            global user_name
            user_name=username
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("invalid login")
    else:
        return render(request,'your_diary_app/login.html',{})

def write(request):

        if request.method=='POST':
            diary_form=Diary_Page_Form(data=request.POST)
            if diary_form.is_valid():
                diary_form.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                print(diary_form.errors)
        else:
            diary_form=Diary_Page_Form()
        return  render(request,'your_diary_app/write.html',{'diary_form':diary_form})

def view(request):
    if request.method=="POST":
        date=request.POST.get('date')
        diary_note=Diary_Page.objects.filter(name=user_name,date=date)
        if diary_note:
            return render(request,'your_diary_app/view.html',{'date':diary_note[0].date,'title':diary_note[0].title,'note':diary_note[0].note})
        else:
            return HttpResponse("no content")
