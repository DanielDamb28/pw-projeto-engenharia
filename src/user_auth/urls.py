from django.conf.urls import include, url
from django.urls import path

from .views import cadastro_view, login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('logout/', logout_view, name='logout'),
]