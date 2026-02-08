from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('houses/', views.houses_list, name='houses'),
    path('house/<int:id>/', views.house_detail, name='house_detail'),
    path('apartment/<int:id>/create-act/', views.create_act, name='create_act'),
]
