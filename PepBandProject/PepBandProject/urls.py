from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from PepBandApp import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),  # Redirect root to login page
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_instrument/', views.add_instrument, name='add_instrument'),
    path('delete_instrument/<int:instrument_id>/', views.delete_instrument, name='delete_instrument'),
    path('<int:student_id>/<str:instrument_id>/', views.assign_instrument, name='assign_instrument'),
]
