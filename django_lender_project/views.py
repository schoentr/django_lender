from django.shortcuts import render


def home_view(request):
    """
    This fuction renders the  home page
    """

    return render(request, 'generic/home.html',)  