from django.contrib import admin
from django.urls import path
from wscubtech import views

urlpatterns = [
    path('', views.Form, name='home'),
    path('admin/', admin.site.urls),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('Form/', views.Form, name='Form'),
]
