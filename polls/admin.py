from django.contrib import admin
from polls.models import Choice, Poll#, Page

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
#class PageInline(admin.TabularInline):
#    model = Page
 #   extra = 0

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] #, PageInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin)
#admin.site.register(Page)

