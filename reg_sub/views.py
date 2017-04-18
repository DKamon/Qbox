from django.shortcuts import render
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from reg_sub.forms import subform, internform
from reg_sub.models import Intern, Subscribe
import json

# Create your views here.


def home(request):
    if request.method == 'POST':
        flag = request.POST['id']
        if flag == 'sub':
            form = subform(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                us = Subscribe(email=cd['email'], name=cd['name'], subject=cd['subject'])
                us.save()
            form1 = subform()
            form2 = internform()
            return render(request, 'reg_sub/index.html', {'alert': 1, 'form': form1, 'form2': form2})
        elif flag == 'intern':
            form = internform(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                us = Intern(email=cd['email'], name=cd['name'], contactno=cd['contactno'], interests=cd['interests'])
                us.save()
            form1 = subform()
            form2 = internform()
            return render(request, 'reg_sub/index.html', {'alert': 2, 'form': form1, 'form2': form2})
        else:
            form1 = subform()
            form2 = internform()
            return render(request, 'reg_sub/index.html', {'alert': 0, 'form': form1, 'form2': form2})
    else:
        form1 = subform()
        form2 = internform()
        return render(request, 'reg_sub/index.html', {'alert':0, 'form': form1, 'form2': form2})

'''
def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/reg/')
    else:
        if request.method == 'POST':
            form = signupform(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                username2 = cd['username']
                name2 = cd['name']
                email2 = cd['email']
                password2 = cd['password2']
                profile2 = cd['profile']
                contact2 = cd['contactno']
                college2 = cd['college']
                us = Qboxuser(name = name2, contactno = contact2 , username = username2, email=email2, profile = profile2, college = college2)
                us.set_password(password2)
                us.save()
                return HttpResponseRedirect('/reg/')
            else:
                return render(request, 'reg_sub/signup.html', {'form': form})
        else:
            form = signupform()
            return render(request, 'reg_sub/signup.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = subform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            us = Subscribe(email=cd['email'])
            us.save()
            return HttpResponseRedirect('/reg/')
        else:
            return render(request, 'reg_sub/subscribe.html', {'form': form})
    else:
        form = subform()
        return render(request, 'reg_sub/subscribe.html', {'form': form})
'''
