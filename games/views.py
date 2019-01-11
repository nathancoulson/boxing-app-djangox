from django.shortcuts import render
from .forms import RoundForm
from .forms import FightForm
from .models import Round
from .models import Fight
from .models import Game
from users.models import CustomUser
from datetime import datetime
# Create your views here.


def create_fight_view(request):
    form = FightForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FightForm()
    context = {
        'form': form
    }
    return render(request, "games/create_fight.html", context)

def all_fights_view(request):
    queryset = Fight.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "games/all_fights.html", context)


def game_view(request, fight_id, user_id):

    user = CustomUser.objects.get(id=user_id)
    fight = Fight.objects.get(id=fight_id)

    Game.objects.create(user_id = user, fight_id = fight, time_created = datetime.now())
    game = Game.objects.filter(user_id = user_id, fight_id = fight_id).order_by('-id')[0]

    form = RoundForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RoundForm()


    context = {
        'game_id': game.id,
        'user_id': game.user_id,
        'fight_id': game.fight_id,
        'boxer_1': fight.boxer_1,
        'boxer_2': fight.boxer_2,
        'start_time': game.time_created,
        'form': form,
    }

    return render(request, "games/game.html", context)
