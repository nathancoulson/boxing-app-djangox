from django.shortcuts import render
from .forms import FightForm
from .models import Fight
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

def fight_view(request):
    context = {
        'fight_id': 1
    }
    return render(request, "games/username_1.html", context)
