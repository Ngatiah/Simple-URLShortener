from django.urls import path
from . import views
'''
path('', Home.as_view(), name='home')
path('', views.home, name='home')
'''
urlpatterns = [
    path("", views.home, name="home"),
    path("api/shorten/", views.api_shorten, name="api_shorten"),
    path("<str:short_code>/", views.redirect_view, name="redirect"),
]