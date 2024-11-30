from .views import *
from django.urls import path,include
urlpatterns = [
    # path('g/',views.index,name="get" ),
    path('p_db/',db,name="print_db" ),
   # print_db path('p/',Run.as_view(),name="print" ),

]