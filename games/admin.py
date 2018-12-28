from django.contrib import admin

# Register your models here.

from .models import Fight
from .models import Game



admin.site.register(Fight)
admin.site.register(Game)
