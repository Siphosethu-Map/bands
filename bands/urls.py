from django.urls import path
from . import views


# all the apps pages urls
app_name = 'bands'
urlpatterns = [
    path('', views.home, name='home'),  # landing page for the app
    path('login', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('authenticate_user/', views.authenticate_user, name='authen_user'),
    path('<int:band_id>/bands/', views.band_details, name='band_details'),
    path('about/', views.about, name='about'),
    path('add-band/', views.add_band, name='add_band'),
    path('log_out/', views.log_out, name='log_out')
]
