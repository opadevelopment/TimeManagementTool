from django.contrib import admin

# Register your models here.

from .models import Kurssi, Teht

admin.site.register(Kurssi)
admin.site.register(Teht)
