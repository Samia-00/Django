from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def index(request):
    # my_dict = {'insert_me': "Hello I am from views.py!!!!"}
    # return render(request,'appTwo/index.html', context=my_dict)
    return HttpResponse("<em>MY SECOND PAGE</em>")

def help(request):
    helpdict =  {'help_insert' : 'HELP PAGE'}
    return render(request, 'appTwo/help.html',context=helpdict)
