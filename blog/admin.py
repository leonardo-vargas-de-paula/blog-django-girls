from django.contrib import admin

from blog.models import Post


class AdminPost(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'created_date')
    search_fields = ['title', 'author']

admin.site.register(Post, AdminPost)