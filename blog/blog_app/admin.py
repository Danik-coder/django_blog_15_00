from django.contrib import admin
from .models import Category, FAQ, Slider, Post, PostGallery, Comment

# фаил отвечающий за отображение таблиц в админ панель

class PostGalleryInline(admin.StackedInline):
    model = PostGallery

class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'published_at', 'category']
    list_display_links = ['title']
    inlines = [PostGalleryInline]


admin.site.register(Category)
admin.site.register(FAQ)
admin.site.register(Slider)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)