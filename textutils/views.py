# I have created this file

# Import needed libraries
from django.http import HttpResponse
from django.shortcuts import render
import string


# The Home sweet Home Page
def home(request):
    return render(request, "home.html")


# The Analyse Page LOGIC
def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Get the filter info from the HTML
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspacemover = request.POST.get('extraspacemover', 'off')

    # Logic
    if removepunc == "on":
        analysed = djtext.translate(djtext.maketrans('', '', string.punctuation))

    if fullcaps == "on":
        analysed = djtext.upper()


    if(extraspacemover=="on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analysed = analysed + char

    if (newlineremover == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analysed = analysed + char
    
    # Render the HTML template
    params = {
        "purpose" : "Hey",
        "analysed_text" : analysed
    }
    return render(request, "analyse.html", params)

def contact(request):
    return render(request, "contact.html")


