from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('health/', views.health_check, name='health'),
]