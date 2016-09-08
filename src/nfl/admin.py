from django.contrib import admin

# Register your models here.
from .models import Question 

class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date"]
    list_display_link = ["question_text", "pub_date"]
    list_filter = ["question_text","pub_date"]
    search_fields = ["question_text", "pub_date"]
    class Meta:
        model = Question 

admin.site.register(Question, QuestionModelAdmin)