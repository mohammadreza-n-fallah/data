from .views import *
from django.urls import path,include
urlpatterns = [
    path('l/',Login.as_view(),name="login" ),

]