from django.contrib import admin

from .models import User, ExampleModel

admin.site.register(User)
admin.site.register(ExampleModel)