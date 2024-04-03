from django.contrib import admin
from venture_app.models import Member, Investor, Blog
# Register your models here.

admin.site.register(Member)
admin.site.register(Investor)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('blog_title',)}

admin.site.register(Blog, BlogAdmin)