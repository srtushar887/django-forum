from django.contrib import admin

# Register your models here.
from .models import Profile

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','user')
    list_display_links = ('id','user')
    list_filter = ('user',)
    list_per_page = 25


admin.site.register(Profile,ImageAdmin)