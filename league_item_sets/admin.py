from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from django.contrib.auth.models import User
from .models import ItemSet, ItemRow

class ItemRowInline(admin.StackedInline):
	model = ItemRow

class ItemSetAdmin(admin.ModelAdmin):
	inlines = [ItemRowInline,]

class ItemSetInline(admin.StackedInline):
	model = ItemSet

class UserAdmin(AuthUserAdmin):
	inlines = [ItemSetInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ItemSet, ItemSetAdmin)