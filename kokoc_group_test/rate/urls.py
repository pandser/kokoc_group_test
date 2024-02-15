from django.urls import path

from . import views


app_name = 'rate'

urlpatterns = [
    path('', views.get_rate)
]
