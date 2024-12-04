from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def simple_view(request):
    data = {"content": "Gfg is the best"}
    return render(request, "index.html", data)

def check_age(request):
    testvar = "thsisatest"
    if request.method == 'POST':
        age = int(request.POST.get('age', 0))
        return render(request, 'check_age.html', {'age': age})
    return render(request, 'check_age.html')

def loop(request):
    data = "Gfg is the best"
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        "data": data,
        "list": number_list
    }
    return render(request, "loop.html", context)

def testcall(request):
    print("Here")
    response = HttpResponse(status_code=201)
    return response

