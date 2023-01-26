from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('', include('gallery.urls')),
    # other URL patterns ...
]
