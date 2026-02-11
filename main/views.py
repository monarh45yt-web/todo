from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "oop.html")

def test(request):
    return render(request, "test.html")
