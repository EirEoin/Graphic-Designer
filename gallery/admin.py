from django.contrib import admin
from .models import PreviousWork


@admin.register(PreviousWork)
class PreviousWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    ordering = ('-date',)
