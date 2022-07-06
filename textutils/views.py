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
    djtext = request.POST.get('text')

    # Get the filter info from the HTML
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    smallcaps = request.POST.get('smallcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspacemover = request.POST.get('extraspacemover', 'off')
    removenumbers = request.POST.get("removenumbers", "off")
    charactercounter = request.POST.get('charactercounter', 'off')
    countspaces = request.POST.get('countspaces', 'off')
    params = {
        "analysed_text": djtext
    }

    # Logic
    if removepunc == "on":
        analysed = djtext.translate(
            djtext.maketrans('', '', string.punctuation))
        djtext = analysed

        params = {
            "analysed_text": analysed
        }

    if fullcaps == "on":
        analysed = djtext.upper()
        djtext = analysed

        params = {
            "purpose": "Full Caped!",
            "analysed_text": analysed
        }

    if smallcaps == "on":
        analysed = djtext.lower()
        djtext = analysed

        params = {
            "analysed_text": analysed
        }

    if extraspacemover == "on":
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed += char
        djtext = analysed

        params = {
            "analysed_text": analysed
        }
    
    if removenumbers == "on":
        analysed = ''.join([char for char in djtext if not char.isdigit()])
        djtext = analysed

        params = {
            "analysed_text": analysed
        }
        

    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed += char
        djtext = analysed

        params = {
            "analysed_text": analysed
        }

    if charactercounter == "on":
        count = 0
        if countspaces == "on":
            for char in djtext:
                count += 1
            params = {
                "analysed_text": f"Words Counted: {count}"
            }

        elif countspaces == "off":
            for char in djtext:
                if char != " ":
                    count += 1
            params = {
                "analysed_text": f"Words Counted: {count}"
            }

    return render(request, "analyse.html", params)


def contact(request):
    return render(request, "contact.html")