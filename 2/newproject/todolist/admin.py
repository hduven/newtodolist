from django.contrib import admin


from .models import Category, Todo, Description

admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Description)