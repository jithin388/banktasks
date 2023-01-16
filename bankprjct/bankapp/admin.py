from django.contrib import admin
from . models import State
from . models import City
from . models import Category
from . models import Gold
# Register your models here.
admin.site.register(State)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Gold)