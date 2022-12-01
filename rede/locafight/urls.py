from django.urls import path
import . from views

urlpatterns = [
    path('', views.home, name='home' ),)
]