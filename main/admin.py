from django.contrib import admin
from .models.models import Devices, Specification, User, Comment
# Register your models here.
admin.site.register(Devices)
admin.site.register(Specification)
admin.site.register(User)
admin.site.register(Comment)