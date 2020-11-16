from django.urls import path
from .views import hopscotch_home, hopscotch_create

app_name = 'hopscotch-urls'

urlpatterns = [
    path('home/', hopscotch_home, name='hopscotch-home'),
    path('create/', hopscotch_create, name='hopscotch-create')
]