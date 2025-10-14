from .models import Student
from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','course','join_date')

admin.site.register(Student,StudentAdmin)