from django.contrib import admin

# Register your models here.
from .models import Student, Group, Role

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Role)