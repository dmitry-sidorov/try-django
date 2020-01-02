from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print('User:', request.user)
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 42,
        "my_list": [234, 87, 12],
        "my_html": "<h1>Hello HTML</h1>"
    }
    return render(request, 'about.html', my_context)