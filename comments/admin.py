# comments/admin.py
from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vacancy', 'content_short', 'created_at')
    list_filter = ('created_at', 'is_active')
    search_fields = ('content', 'user__username', 'vacancy__title')

    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_short.short_description = 'Matn'