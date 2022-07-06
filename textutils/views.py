# I have created this file

# Import needed libraries
from django.http import HttpResponse
from django.shortcuts import render
import string


# The Home sweet Home Page
def home(request):
    return render(request, "home.html")


# The Analyse Page LOGIC
def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Get the filter info from the HTML
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspacemover = request.GET.get('extraspacemover', 'off')
    charactercounter = request.GET.get('charactercounter', 'off')
    countspaceornot = request.GET.get('countspaceornot', 'off')

    # Code the logic
    if removepunc == "on":
        analysed = djtext.translate(djtext.maketrans('', '', string.punctuation))

    elif fullcaps == "on":
        analysed = djtext.upper()

    elif newlineremover == "on":
        analysed = djtext.rstrip()
    
    elif extraspacemover == "on":
        analysed = " ".join(djtext.split())

    elif charactercounter == "on":
        count = 0
        for char in djtext:
            if countspaceornot == "on":
                count += 1
            elif char != " ":
                count += 1
        analysed = str(count)
    else:
        analysed = djtext

    # The params which are supposed to be passed on the render fucntion so the variables can be accessed in the HTML
    params = {
    "purpose" : "Removed Punctuations",
    "analysed_text" : analysed,
    }

    # Render the HTML template
    return render(request, "analyse.html", params)

def contact(request):
    return render(request, "contact.html")


