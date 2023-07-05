from django.urls import path
from . import views


app_name = 'Food'

urlpatterns = [
    path('',views.index, name = 'index'),    # Name Parameter is used for removing the hardcoded urls
    path('<int:item_id>/',views.detail, name = "detail"),  # It is used by removing url from href and user 
                                                           # name given for the particular url
]