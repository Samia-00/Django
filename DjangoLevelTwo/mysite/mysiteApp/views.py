# from django.http import request
from django.shortcuts import render
# from mysiteApp.models import User
from mysiteApp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'mysiteApp/index.html')

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request,'mysiteApp/users.html',{'form':form})

    # user_list = User.objects.order_by("first_name")
    # user_dict = {'users': user_list}
    # return render(request,'mysiteApp/users.html', context=user_dict)