from django.urls import path
from django.views.generic import RedirectView
from django.contrib import admin
from PepBandApp import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),  # Redirect root to login page
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('add_instrument/', views.add_instrument, name='add_instrument'),
    path('delete_instrument/', views.delete_instrument, name='delete_instrument'),
    path('assign_instrument/', views.assign_instrument, name='assign_instrument'),
    path('unassign_instrument/', views.unassign_instrument, name='unassign_instrument'),
]
