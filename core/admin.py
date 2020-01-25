from django.contrib import admin
from .models import Feedback, Subject, Author
# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'is_active', 'created_at')
    list_editable = ('is_active', )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'bot_name', 'is_active', 'author')
    list_editable  = ('is_active', 'author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
