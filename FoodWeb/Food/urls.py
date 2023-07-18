from django.urls import path
from . import views


app_name = 'Food'

urlpatterns = [
    path('',views.index, name = 'index'),    # Name Parameter is used for removing the hardcoded urls
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    # path('<int:item_id>/',views.detail, name = "detail"),  # It is used by removing url from href and user 
                                                           # name given for the particular url
    path('add/',views.CreateItem.as_view(),name = 'create_item'),
    path('update/<int:id>/', views.item_update, name = 'update_item'),
    path('delete/<int:id>/', views.item_delete, name = 'delete_item'),
]