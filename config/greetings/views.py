from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def say_hello(request: HttpRequest) -> HttpResponse:
    name = request.GET.get('name')
    message = request.GET.get('message')
    if name is not None and message is not None:
        return HttpResponse(f"<h2>Hello {name}! {message}")
    return HttpResponse(f"<h2>Hello Rekruto! Давай дружить!")
