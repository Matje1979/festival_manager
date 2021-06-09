from django.contrib import admin
from .models import Event, Visitor
from django_admin_inline_paginator.admin import TabularInlinePaginated



class VisitorInline(TabularInlinePaginated):
	model = Visitor
	fields = ('first_name', 'last_name', 'email')
	per_page = 5

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	class Media:
		css={
		    'all': ('css/admin/manager_admin.css',)
		}

	inlines = (
        VisitorInline,
	)


# admin.site.register(Event, EventAdmin)
admin.site.register(Visitor)

# Register your models here.
