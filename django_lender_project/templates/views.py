from django.shortcuts import render


def home_view(request):
    return render(request, 'generic/home.html', context={'message':'whassup!'})  #context used in rendered
    