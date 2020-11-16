from django.urls import path
from .views import writer_home, writer_profile, create_user, view_profile, login_writer, logout_writer

app_name='accounts-urls'

urlpatterns = [
    path('', writer_home, name='writer-home'),
    path('profile/', writer_profile, name='writer-profile'),
    path('create/', create_user, name='create-user'),
    path('view-profile/<str:email>', view_profile, name='view-profile'),
    path('login/', login_writer, name='login'),
    path('logout/', logout_writer, name='logout'),
]
