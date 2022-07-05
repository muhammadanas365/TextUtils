# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, "index.html")

def analyze(request):
   # Get the text
   djtext = request.GET.get('text', 'default')
   removepunc = request.GET.get('removepunc', 'off')
   analysed = djtext.translate(djtext.maketrans('', '', string.punctuation))
   params = {
    "purpose" : "Removed Punctuations",
    "analysed_text" : analysed,
   }

   # Analyse the text
   return render(request, "analyse.html", params)


