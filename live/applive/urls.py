from django.urls import path
from . import views

app_name = 'applive'

urlpatterns = [
    path('', views.home_action, name='home'),
    path('settings/', views.settings, name='settings'),

]
