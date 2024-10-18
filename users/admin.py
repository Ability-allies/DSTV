from django.contrib import admin
from .models import Parent, Child, Advice, TherapySession, Journal

# Register the Parent model
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    
    list_filter = ('user',)
    ordering = ('user',)

# Register the Child model
@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')
    search_fields = ('name',)
    list_filter = ('gender',)
    ordering = ('name',)

# Register the Advice model
@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ('category', 'date', 'advice')
    search_fields = ('advice',)
    list_filter = ('category', 'date')
    ordering = ('date',)

# Register the TherapySession model
@admin.register(TherapySession)
class TherapySessionAdmin(admin.ModelAdmin):
    list_display = ('category', 'date', 'therapy_content')
    search_fields = ('therapy_content',)
    list_filter = ('category', 'date')
    ordering = ('date',)

# Register the Journal model
@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('child', 'parent', 'time')
    search_fields = ('entry',)
    list_filter = ('child', 'parent', 'time')
    ordering = ('time',)
