from django.contrib import admin
from life.models import Event, Categories

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'timestamp')
	ordering = ['timestamp']
	date_hierarchy = ('timestamp')
	list_filter = ['category', 'counterUnit']
	search_fields = ['title']

class CategoriesAdmin(admin.ModelAdmin):
	pass

admin.site.register(Event, EventAdmin)
admin.site.register(Categories, CategoriesAdmin)