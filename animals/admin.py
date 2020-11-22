from django.contrib import admin
from .models import Animals
from .models import Fruits
from .models import Colours

# Register your models here.

admin.site.register(Animals)
admin.site.register(Fruits)
admin.site.register(Colours)