from customapp import views
from django.urls import path

urlpatterns = [
    path('custom',views.custom),
    path('register',views.Register),
    path('login',views.login),
]