from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def index(request):
    # Define the data you want to pass to the template
    my_dict = {'insert_me': "Hello, I am from views.py!!!!"}

    # Render the template with the data
    return render(request, 'oneApp/index.html', context=my_dict)


# def index(request):
#     my_dict = {'insert_me': "Hello I am from views.py!!!!"}
#     return render(request,'oneApp/index.html', context=my_dict)

# def help(request):
#     helpdict =  {'help_insert' : 'HELP PAGE'}
#     return render(request, 'oneApp/help.html',context=helpdict)