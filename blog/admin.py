from django.contrib import admin
from .models import Documentry, News, Story, Food, Travel, comment
# Register your models here.

@admin.register(Documentry)
class DocumentryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','image','description','created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','image','description','created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','image','description','created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','image','description','created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','image','description','created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('d_relation', 's_relation','f_relation','t_relation')
    search_fields = ('d_relation',)
    list_filter = ('d_relation',)