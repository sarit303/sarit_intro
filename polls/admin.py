from django.contrib import admin
from polls.models import Choice, Poll
from django.utils import timezone
import datetime

class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 3
    extra = 0
        
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] 
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

    def save_model(self, request, obj, form, change):
        if obj.has_write_in:
            try:
                # create a new Choice with is_other_choice = True
                # add the OtherChoice to this poll
                pass
            except:
                # error message?
                pass
        obj.save()
    
admin.site.register(Poll, PollAdmin)