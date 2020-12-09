from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):

    #displays question text as well as date in listing screen of admin
    list_display = ( 'pk','question_text', 'pub_date', 'was_published_recently')

    #Customizing add/edit screen 
    fieldsets = [
        ('Question',{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    #filters
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)