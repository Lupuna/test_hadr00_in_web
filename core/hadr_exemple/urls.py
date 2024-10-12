from django.urls import path, include
from hadr_exemple.views import HadrZeroZeroAPIView

urlpatterns = [
    path('Hadr00/', HadrZeroZeroAPIView.as_view(), name='hadr_zero_zero')
]
