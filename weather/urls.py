from  django.urls import path
from weather.views import Home

app_name = 'weather'
urlpatterns = [
    path('',Home.as_view(),name='home'),
]
