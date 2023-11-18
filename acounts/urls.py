from django.urls import path
from .views import login_user, logout_user, page_login


urlpatterns = [
   
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('', login_user, name='page_login'),
    
]