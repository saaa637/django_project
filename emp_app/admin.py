from django.contrib import admin

# Register your models here.
from .models import Person, Department, Role

admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Role)

