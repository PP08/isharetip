from django.contrib import admin
from .models import Post, Category, Author, UserProfile
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category', 'title', 'author', 'created_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(UserProfile)
