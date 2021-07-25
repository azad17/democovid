from django.urls import path
from .import views
app_name='book'
urlpatterns = [
    path('',views.home,name='home'),
    path('booking/',views.booking,name='booking'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('contact',views.contact,name='contact'),
    path('expert/<int:pk>/',views.expert,name='expert'),
    #ajax
    path('ajax/load-center/',views.load_center,name='ajax_load_center'),
]