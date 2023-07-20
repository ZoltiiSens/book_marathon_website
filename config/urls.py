from django.contrib import admin
from django.urls import path
from app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name='indexPage'),
    path('Margo/', views.MargoUpdate, name='MargoUpdate'),
    path('Roma/', views.RomaUpdate, name='RomaUpdate'),
]
