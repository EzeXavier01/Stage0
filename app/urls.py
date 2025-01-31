from app.views import info
from django.urls import path

urlpatterns = [
    path('info/', info),
]
