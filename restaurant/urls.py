from django.urls import path
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view())
]
