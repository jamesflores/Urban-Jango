from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('define/', views.define, name='define'),
    path('about/', views.about, name='about'),
]