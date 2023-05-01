from greetings.views import say_hello
from django.urls import path


urlpatterns = [
    path('', say_hello, name='say_hello'),
]
