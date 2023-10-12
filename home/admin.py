from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(student)
admin.site.register(category)
admin.site.register(book)