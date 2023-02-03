from django.contrib import admin

from apps.blog.models import Blog, Category, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'enabled')
    search_fields = ('title', 'body')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment)
