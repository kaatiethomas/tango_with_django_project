from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    #determines order on individual pages
    list_display = ('title', 'category',  'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)