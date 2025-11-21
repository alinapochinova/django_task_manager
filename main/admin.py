from django.contrib import admin
from .models import Task, Category
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'deadline', 'category', 'executor')
    list_filter = ('is_done', 'category')
    search_fields = ('title',)
admin.site.register(Category)
# Register your models here.
