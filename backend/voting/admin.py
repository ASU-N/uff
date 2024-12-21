from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'party')  # Columns to display in the admin list view
    search_fields = ('name', 'party')  # Add search functionality
    list_filter = ('party',)  # Add filtering options
    ordering = ('id',)  # Default ordering

