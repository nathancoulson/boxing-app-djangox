from django.urls import path

from .views import create_fight_view, fight_view, all_fights_view

urlpatterns = [
    path('create_fight/', create_fight_view, name='create_fight'),
    path('username_1/', fight_view, name='fight'),
    path('all_fights/', all_fights_view, name='all_fights'),

]
