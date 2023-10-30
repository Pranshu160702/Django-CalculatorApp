from django.http import HttpRequest
from django.shortcuts import render

def indexPage(request):
    a = ""
    ans = a
    if request.method == "POST":
            a = str(request.POST.get('equation'))
            try:
                ans = eval(a)
            except:
                pass
    data = {
        'output': ans
    }
    return render(request, "index.html",data)