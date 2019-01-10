from django.urls import path

from .views import create_fight_view, game_view, all_fights_view

urlpatterns = [
    path('create_fight/', create_fight_view, name='create_fight'),
    path('all_fights/', all_fights_view, name='all_fights'),
    path('game/<int:fight_id>/<int:user_id>/', game_view, name='game'),

]
