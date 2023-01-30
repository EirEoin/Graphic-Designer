from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.work, name='work'),
    path('previous-work/', views.previous_work, name='previous_work'),
    # other URL patterns ...
]
