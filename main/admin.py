from django.contrib import admin
from .models.models import Devices, Specification, User, Comment
# Register your models here.
@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ("name", "model")

@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ("processor", "ram", "memory", "battery", "size")

admin.site.register(User)
admin.site.register(Comment)