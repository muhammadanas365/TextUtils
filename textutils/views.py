# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
   # Get the text
   djtext = request.GET.get('text', 'default')
   removepunc = request.GET.get('removepunc', 'off')
   print(removepunc)
   print(djtext)

   # Analyse the text
   return HttpResponse(f"Your text: {djtext}")


