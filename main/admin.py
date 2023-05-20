from django.contrib import admin
from .models.models import *
# Register your models here.
admin.site.register(Devices)
admin.site.register(Specification)
admin.site.register(Specification_type)
admin.site.register(User)
admin.site.register(Comment)