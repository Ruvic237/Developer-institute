from django.urls import path
from .views import people, peoples

urlpatterns = [
    path('peoples/', peoples, name="ok"),
    path('people/<int:id>', people, name="ok2"),
]

