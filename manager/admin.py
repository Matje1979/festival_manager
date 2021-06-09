from django.contrib import admin
from .models import Event, Visitor
from django_admin_inline_paginator.admin import TabularInlinePaginated



class VisitorInline(TabularInlinePaginated):

	model = Visitor
	readonly_fields = ('first_name', 'last_name', 'email', 'applied_at') #readonly_fields instead of fields to make applied at field visible in admin 
	per_page = 10    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

	model = Event
	list_per_page=10  #Number of records to show on one page

	class Media:

		css={
		    'all': ('css/admin/manager_admin.css',)
		}

	inlines = (
        VisitorInline,
	)
	
admin.site.register(Visitor)

