from django.urls import path
from .views import *

urlpatterns = [
    
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('logout/', UserLogout.as_view(), name='logout'),

]
