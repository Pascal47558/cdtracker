from django.contrib import admin

# Register your models here.
from .models import CD, Group

admin.site.register(CD)
admin.site.register(Group)