from . import views
from django.urls import path,include
urlpatterns = [
    path('p/',views.db,name="print" ),

]