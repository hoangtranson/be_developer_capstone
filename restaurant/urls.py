from django.urls import path
from restaurant.views import say_hello

urlpatterns = [
    path('', say_hello, name='sayHello'),
]