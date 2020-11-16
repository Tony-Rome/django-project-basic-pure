"""backend_rayuela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import preview_page, login_page, logout_page

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', preview_page, name='init-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', logout_page, name='logout-page'),
    path('story/', include('stories.urls', namespace='stories-urls')),
    path('writers/', include('writers.urls', namespace='writers-urls')),
    path('accounts/', include('accounts.urls', namespace='accounts-urls')),
    path('hopscotch', include('hopscotch.urls', namespace='hopscotch-urls')),
    path('stories-routes/', include('stories_routes.urls', namespace='stories-routes-urls'))
]


if settings.DEBUG:
    urlpatterns+= staticfiles_urlpatterns()
