from django.shortcuts import render


def homepage(request):
    return render(request, 'chat/homepage.html',
                  {'chat': homepage})
