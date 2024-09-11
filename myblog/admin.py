from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostLike)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary']