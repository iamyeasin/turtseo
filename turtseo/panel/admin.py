from django.contrib import admin 
from .models import Key_Link_List, Niche, Column_Set, Profile, Profile_Extended

class Key_LinkAdmin(admin.ModelAdmin):
	list_display = ('key_link',)
	list_display_links = ('key_link',)
	search_fields = ('key_link',)
	list_per_page = 30

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('key_link','url','domanin_rank')
	list_display_links = ('key_link','domanin_rank')
	search_fields = ('key_link','url')
	list_per_page = 30

class Profile_ExtendedAdmin(admin.ModelAdmin):
	list_display = ('key_link','domanin_auth','spam_score')
	list_display_links = ('key_link','domanin_auth')
	list_per_page = 30

admin.site.register(Key_Link_List, Key_LinkAdmin)
admin.site.register(Niche)
admin.site.register(Column_Set)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile_Extended, Profile_ExtendedAdmin)
