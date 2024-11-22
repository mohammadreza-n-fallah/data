from .views import *
from django.urls import path,include
urlpatterns = [
    # path('g/',views.index,name="get" ),
    path('p/',Run.as_view(),name="print" ),

]