from django.shortcuts import render

def authority(request):
    return render(
        request,
        'authority/index.html'
    )