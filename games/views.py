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

def game_view(request, fight_id, user_id, game_id):

    user = CustomUser.objects.get(id=user_id)
    fight = Fight.objects.get(id=fight_id)

    if game_id == 0:
        Game.objects.create(user_id = user, fight_id = fight, time_created = datetime.now())
        game = Game.objects.filter(user_id = user_id, fight_id = fight_id).order_by('-id')[0]
    else:
        game = Game.objects.get(id=game_id)


    form = RoundForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RoundForm()


    context = {
        'game_id': game.id,
        'user_id': game.user_id,
        'fight_id': fight.id,
        'boxer_1': fight.boxer_1,
        'boxer_2': fight.boxer_2,
        'start_time': game.time_created,
        'form': form,
    }

    return render(request, "games/game.html", context)

def result_view(request, fight_id, game_id):
    game_data = Round.objects.filter(game_id = game_id)
    fight_details = Fight.objects.get(id = fight_id)
    context = {
        "game_id": game_id,
        "fight_id": fight_id,
        "object_list": game_data,
        "boxer_1": fight_details.boxer_1,
        "boxer_2": fight_details.boxer_2,
    }
    return render(request, "games/result.html", context)

def who_won_view(request, fight_id, game_id):
    game_data = Round.objects.filter(game_id = game_id)
    fight_details = Fight.objects.get(id = fight_id)


    fight_dict = {}
    # fight_dict = {
    #     1: {},
    #     2: {},
    #     3: {},
    #     4: {},
    #     5: {},
    #     6: {},
    #     7: {},
    #     8: {},
    #     9: {},
    #     10: {},
    #     11: {},
    #     12: {},
    # }

    for round in game_data:
        if round.boxer_1_knockdowns > round.boxer_2_knockdowns:
            fight_dict[round.round_number] = {"boxer_1": 8, "boxer_2": 10}
            if round.boxer_1_hits - round.boxer_2_hits > 30:
                fight_dict[round.round_number] = {"boxer_1": 9, "boxer_2": 10}
        elif round.boxer_2_knockdowns > round.boxer_1_knockdowns:
            fight_dict[round.round_number] = {"boxer_1": 10, "boxer_2": 8}
            if round.boxer_2_hits - round.boxer_1_hits > 30:
                fight_dict[round.round_number] = {"boxer_1": 10, "boxer_2": 9}
        elif round.boxer_1_knockdowns == round.boxer_2_knockdowns:
            if round.boxer_1_hits > round.boxer_2_hits:
                fight_dict[round.round_number] = {"boxer_1": 10, "boxer_2": 9}
                if round.boxer_1_hits - round.boxer_2_hits > 40:
                    fight_dict[round.round_number]["boxer_2"] = 8
            elif round.boxer_2_hits > round.boxer_1_hits:
                fight_dict[round.round_number] = {"boxer_1": 9, "boxer_2": 10}
                if round.boxer_2_hits - round.boxer_1_hits > 40:
                    fight_dict[round.round_number]["boxer_1"] = 8
            else:
                fight_dict[round.round_number] = {"boxer_1": 10, "boxer_2": 10}

    # for round in game_data:
    #     if round.boxer_1_hits > round.boxer_2_hits:
    #         fight_dict[round.round_number] = {"boxer_1": 10, "boxer_2": 9}
    #         if round.boxer_1_hits - round.boxer_2_hits > 40:
    #             fight_dict[round.round_number]["boxer_2"] = 8
    #     elif round.boxer_2_hits > round.boxer_1_hits:
    #         fight_dict[round.round_number] = {"boxer_1": 9, "boxer_2": 10}
    #         if round.boxer_2_hits - round.boxer_1_hits > 40:
    #             fight_dict[round.round_number]["boxer_1"] = 8
    #     else:
    #         fight_dict[round.round_number] = {"boxer_1": 10, "boxer_2": 10}


    for round in game_data:
        # fight_dict[round.round_number]["boxer_1"] -= int(round.boxer_1_knockdowns)
        fight_dict[round.round_number]["boxer_1"] -= int(round.boxer_1_penalties)
        # fight_dict[round.round_number]["boxer_2"] -= int(round.boxer_2_knockdowns)
        fight_dict[round.round_number]["boxer_2"] -= int(round.boxer_2_penalties)

    # for round in game_data:
    #     fight_dict[round.round_number]["boxer_1"] -= int(round.boxer_1_knockdowns)
    #     fight_dict[round.round_number]["boxer_1"] -= int(round.boxer_1_penalties)
    #     fight_dict[round.round_number]["boxer_2"] -= int(round.boxer_2_knockdowns)
    #     fight_dict[round.round_number]["boxer_2"] -= int(round.boxer_2_penalties)

    boxer_1_rounds = 0
    boxer_2_rounds = 0

    for key, value in fight_dict.items():
        print(key, value)

    for value in fight_dict.values():
        if value["boxer_1"] > value["boxer_2"]:
            boxer_1_rounds += 1
        elif value["boxer_2"] > value["boxer_1"]:
            boxer_2_rounds += 1

    if boxer_1_rounds > boxer_2_rounds:
        winner = fight_details.boxer_1
    elif boxer_2_rounds > boxer_1_rounds:
        winner = fight_details.boxer_2
    else:
        winner = "No one! It's a draw"


    context = {
        "fight_dict": fight_dict,
        "winner": winner,
        "game_id": game_id,
        "object_list": game_data,
        "boxer_1": fight_details.boxer_1,
        "boxer_2": fight_details.boxer_2,
    }
    return render(request, "games/who_won.html", context)
