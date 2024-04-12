from django.contrib import admin
from .models import category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('category_name',)}
    list_display = ('slug',)
admin.site.register(category,CategoryAdmin)
