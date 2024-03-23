from customapp import views
from django.urls import path
from django.urls import path
from .views import verify_email


urlpatterns = [
    path('',views.custom),
    path('register',views.Register),
    path('login',views.login),
    path('verify_email/', verify_email, name='verify_email'),

    
]