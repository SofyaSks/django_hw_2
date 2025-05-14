from django.shortcuts import render

def facts(request):
    context = {
        'facts': 'Факты о городе'
    }
    return render(
        request,
        'facts/index.html',
        context
    )
