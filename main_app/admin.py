from django.contrib import admin
from .models import Chapter,Volume, Exercise, Solution

# Register your models here.
admin.site.register(Chapter)
admin.site.register(Volume)
admin.site.register(Exercise)
admin.site.register(Solution)
