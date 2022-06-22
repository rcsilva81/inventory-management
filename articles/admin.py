from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_per_page = 10

admin.site.register(Article, ArticleAdmin)