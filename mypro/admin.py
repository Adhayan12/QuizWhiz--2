from django.contrib import admin
from .models import Feature
from .models import question
from .models import QuizResult

# Register your models here.

admin.site.register(Feature)
admin.site.register(question)
admin.site.register(QuizResult)
