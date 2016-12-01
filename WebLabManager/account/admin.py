from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'supervisor','join_date','CID','position']

class UserAdmin(admin.ModelAdmin):
    list_display = ('user','supervisor','position','user_type','status' )
    list_filter = ('supervisor','position','user_type','status')
    search_fields = ('description','user','supervisor','position')
    # raw_id_fields = ('name',)
    date_hierarchy ='join_date'
    ordering = ('position','supervisor','user')

# admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile,UserAdmin)

# Register your models here.
