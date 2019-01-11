from django.urls import path

from .views import create_fight_view, game_view, all_fights_view, result_view, who_won_view

urlpatterns = [
    path('create_fight/', create_fight_view, name='create_fight'),
    path('all_fights/', all_fights_view, name='all_fights'),
    path('game/<int:fight_id>/<int:user_id>/<int:game_id>/', game_view, name='game'),
    path('game/result/<int:fight_id>/<int:game_id>/', result_view, name='result'),
    path('game/who_won/<int:fight_id>/<int:game_id>/', who_won_view, name='who_won'),

]
