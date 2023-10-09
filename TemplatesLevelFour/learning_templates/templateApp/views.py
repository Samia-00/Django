from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict=  {'text':'Hellow World', 'number': 100}
    return render(request,'templateApp/index.html', context_dict)

def other(request):
    return render(request,'templateApp/other.html')

def relative(request):
    return render(request,'templateApp/relative_url_templates.html')