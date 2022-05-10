from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def analyze(request):
    input_text = request.POST.get('text')
    remove_punc = request.POST.get('removepunc','off')
    full_caps = request.POST.get('fullcaps','off')
    new_line = request.POST.get('newlineremover', 'off')
    space_remove = request.POST.get('spaceremover', 'off')
    char_count = request.POST.get('charactercount', 'off')

    if full_caps == "on":
        upper_case_text = ""
        for char in input_text:
            upper_case_text = upper_case_text+char.upper()
        params = {'analyzed_text':upper_case_text}
        return render(request,"analyze.html",params)

    elif char_count == "on":
        count = 0
        for data in input_text:
            count = count + 1
        params = {'analyzed_text':count}
        return render(request,"analyze.html",params)

    elif new_line == "on":
        cleaned_data = ""
        for item in input_text:
            if item != '\n' and item != '\r':
                cleaned_data = cleaned_data+item
        params = {"analyzed_text":cleaned_data}
        return render(request,"analyze.html",params)

    elif space_remove == "on":
        data = input_text
        data = data.replace(" ","")
        params = {"analyzed_text":data}
        return render(request,"analyze.html",params)

    elif remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$^%&*_~'''
        final_data = ''
        for item in input_text:
            if item not in punctuations:
                final_data = final_data + item
        params = {"analyzed_text":final_data}
        return render(request, "analyze.html", params)