from django.shortcuts import render
from django.http import HttpResponse

def loveBunny(request):
    return render(request, 'Bunny.html')
