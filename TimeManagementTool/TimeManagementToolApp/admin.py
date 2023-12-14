from django.contrib import admin

# Modelien rekisteröinti

from .models import Kurssi, Teht

admin.site.register(Kurssi)
admin.site.register(Teht)
