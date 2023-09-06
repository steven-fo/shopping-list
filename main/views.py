from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Steven Faustin Orginata',
        'class': 'PBP C',
    }

    return render(request, "main.html", context)