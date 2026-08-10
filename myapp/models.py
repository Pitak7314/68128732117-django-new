from django.db import models
from django.urls import reverse
from django.contrib import admin

PREFIX_NAME = (
    ('นาย', 'นาย'),
    ('นาง', 'นาง'),
    ('นางสาว', 'นางสาว')
)

class Major(models.Model):
    major_name = models.CharField(max_length=100)

    def __str__(self):
        return self.major_name

    def get_absolute_url(self):
        return reverse('major_detail', args=[str(self.id)])

class Student(models.Model):
    prefix_name=models.CharField(max_length=10, choices=PREFIX_NAME, default='นาย')
    stu_id=models.CharField(max_length=10, unique=True)
    fname=models.CharField(max_length=50, blank=True)
    lname=models.CharField(max_length=50, blank=True)
    major=models.ForeignKey(Major, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.stu_id+' '+self.fname+' '+self.lname
    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.stu_id)])


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'prefix_name', 'fname', 'lname','major')

admin.site.register(Student,StudentAdmin)


class majorAdmin(admin.ModelAdmin):
    list_display = ("id","major_name")

admin.site.register(Major, majorAdmin)