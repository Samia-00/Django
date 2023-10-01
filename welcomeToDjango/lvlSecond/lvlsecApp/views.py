from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "HELLO I'M FROM FRISTAPP"}
    return render(request,'lvlsecApp/index.html',context=my_dict)