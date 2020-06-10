from django.contrib import admin 
from .models import *

class Key_LinkAdmin(admin.ModelAdmin):
	list_display = ('key_link',)
	list_display_links = ('key_link',)
	search_fields = ('key_link',)
	list_per_page = 30

class Key_Link_Counter(admin.ModelAdmin):
	list_display = ('key_link', 'compare_key_link', 'no_of_data_matched', 'compare_key_link_no_of_data')
	list_display_links = ('key_link', 'compare_key_link')
	search_fields = ('key_link', 'compare_key_link')
	list_per_page = 30

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('key_link','url','domanin_rank')
	list_display_links = ('key_link','url')
	search_fields = ["url"]
	list_per_page = 30

class Profile_ExtendedAdmin(admin.ModelAdmin):
	list_display = ('key_link','domanin_rank','domanin_auth','spam_score')
	list_display_links = ('key_link','domanin_auth')
	list_per_page = 30

class DirectoryNameAdmin(admin.ModelAdmin):
	list_display = ('directory_name',)
	search_fields = ('directory_name',)
	list_per_page = 30

class DirectoryItemAdmin(admin.ModelAdmin):
	list_display = ('directory_name', 'key_link')
	list_display_links = ('key_link',)
	search_fields = ('directory_name',)
	list_per_page = 30


admin.site.register(Key_Link_List, Key_LinkAdmin)
admin.site.register(Niche)
admin.site.register(Column_Set)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile_Extended, Profile_ExtendedAdmin)
admin.site.register(Link_Counter, Key_Link_Counter)
admin.site.register(DirectoryName, DirectoryNameAdmin)
admin.site.register(DirectoryItem, DirectoryItemAdmin)
