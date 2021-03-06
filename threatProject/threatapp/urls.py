from django.urls import path

from . import views

app_name = 'threatapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('uploadfile/', views.uploadfile, name='uploadfile'),
    path('checkupdate/', views.checkupdate, name='checkupdate'),
]