from django.contrib import admin
from .models import *

class ModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date','slug']
    list_filter = ['publishing_date']
    search_fields = ['title']
    class Meta:
        model = Novel

class ModelAdmin2(admin.ModelAdmin):
    list_display = ['novel','chapter_name','chapter_number', 'created_date', ]
    list_filter = ['created_date']
    list_display_links = ['chapter_name']
    search_fields = ['chapter_name','chapter_number']
    class Meta:
        model = Chapter

class ModelAdmin3(admin.ModelAdmin):
    list_display = ['h_title' ]
    list_filter = ['h_created_date']
    list_display_links = ['h_title']
    search_fields = ['h_title']
    class Meta:
        model = Haberler



admin.site.register(Novel,ModelAdmin,)
admin.site.register(Chapter,ModelAdmin2)
admin.site.register(Haberler,ModelAdmin3)
