from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm,ProfileForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def login_view(request):
#     template_name = "accounts/login.html"
#     context={}

#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         if not User.objects.filter(username=username).exists():
#          messages.success(request, "user")
#          context['user_not_found'] = True
#          return render(request,template_name, context)

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "you are login successfully")
#             return redirect('blog:home')
#         else:
#             context['error']=True
#             return render(request, template_name, context)

#     return render(request, template_name, context)
# def login_view(request):
#     template_name = "accounts/login.html"
#     context={}
#     if request.method=='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('pass')
#         if not User.objects.filter(username=username).exists():
#             messages.warning(request, "چنین کاربری وجود ندارد")
#             return render(request, template_name, context)

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             print("<<<<<<>>>>>>>",request.POST)
#             login(request, user)
#             messages.success(request,"شما با موفقیت وارد شدید")
#             return redirect("blog:home")
#         else:
#             messages.error(request, "نام کاربری و یا کلمه عبور اشتباه می باشد")
#             return render(request, template_name, context)

#     return render(request, template_name, context)

def login_view(request):
    template_name = "accounts/login.html"
    form = LoginForm()
    context = {'form':form}
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if not User.objects.filter(username=username).exists():
                messages.warning(request, 'چنین کابری وجود ندارد')
                return render(request, template_name, context)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "شما با موفقیت وارد شدید")
                return redirect('blog:home')
            else:
                messages.info(request,'نام کاربری و یا کلمه عبور صحیح نمی باشد')
                return render(request, template_name, context)
        else:
            messages.error(request, "مشکلی وجود دارد...")

    
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    messages.success(request, 'با آرزوی دیدار مجدد شما کاربر عزیز')
    return redirect("accounts:login")

@login_required
def profile_view(request):
    template_name = 'accounts/profile.html'
    context = {}
    user = request.user
    initial = {
        'bio': user.profile.bio
        }
    form = ProfileForm(request.POST or None, instance=user, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            bio = form.cleaned_data['bio']
            user.profile.bio = bio
            user.profile.save()
            messages.success(request, 'تغییرات کاربری انجام شد')
            return redirect('accounts:profile')
        else:
            context={'form':form}
            return render(request, template_name, context)

    context={'form':form}
    return render(request, template_name, context)


def register(request):
    template_name = 'accounts/register.html'
    context={}
    form = RegisterForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request,"ثبت نام شد با موفقیت انجام شد")
            return redirect("accounts:login")
        else:
            context['form']=form
            return render(request, template_name, context)
    else:
        context['form']=form
       
    return render(request, template_name, context)