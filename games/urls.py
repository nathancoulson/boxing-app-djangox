from django.urls import path

from .views import create_fight_view, fight_view

urlpatterns = [
    path('create_fight/', create_fight_view, name='create_fight'),
    path('username_1/', fight_view, name='fight'),
]
