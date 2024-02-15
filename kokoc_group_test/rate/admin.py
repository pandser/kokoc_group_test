from django.contrib import admin

from .models import Valute


@admin.register(Valute)
class VluteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'charcode',
        'rate',
        'date',
    )