from django.urls import path
from . import views
from django.views.static import serve


app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('shop', views.shop,name='shop'),
]