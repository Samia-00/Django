# from django.http import request
from django.shortcuts import render
from mysiteApp.models import User

# Create your views here.
def index(request):
    return render(request,'mysiteApp/index.html')

def users(request):
    user_list = User.objects.order_by("first_name")
    user_dict = {'users': user_list}
    return render(request,'mysiteApp/users.html', context=user_dict)