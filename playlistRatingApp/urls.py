from django.urls import path
from . import views

urlpatterns = [
    path('simple', views.simple_view),
    path('condition', views.check_age),
    path('loop', views.loop)
]

