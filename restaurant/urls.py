from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, msg

urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),
]
