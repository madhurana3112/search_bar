from django.urls import path
from authentication_app.views import *
urlpatterns = [
        
    path("",signup,name="signup"),
    path("data_dump",data_dump),
    path("login",signin,name="signin"),
    path("verify_otp",verify_otp,name="verify_otp"),
    path('logout/', logout_view, name='logout'),
    
    path('search/', search, name='search'),
    
    path('searched_text', descriptionView, name='avc'),
    
    path('search-page/', search_page, name='search-page'),
    path('country_details/<str:code>', country_details , name='country_details'),
]