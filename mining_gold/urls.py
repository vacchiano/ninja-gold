from django.urls import path
from . import views

app_name = "mining_gold"
urlpatterns = [
    path('', views.index, name="home"),
    path('process_money/', views.processMoney, name="process"),
]