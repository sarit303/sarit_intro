from django.db import models
from django.utils import timezone
import datetime
from django import forms
from django.forms import ModelForm, Textarea
from django.core import validators


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    has_write_in = models.BooleanField(default=False)
    
    # adding a unicode method for better object representation
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now
        was_published_recently.admin_order_field = 'pub_date'
        was_pubilshed_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)  
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0)
    result = models.TextField(blank=True, null=True)
    is_other_choice = models.BooleanField(default=False)

    def __unicode__(self):
        return self.choice_text

class CustomForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'write_in']
    # Creating a form to add an article
#    if write_in == True:
#        form = CustomForm()
#    else: 
#        None
