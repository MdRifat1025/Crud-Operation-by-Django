from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    course = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
