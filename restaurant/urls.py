from django.urls import path
from .views import MenuView, BookingView

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('booking/', BookingView.as_view())
]