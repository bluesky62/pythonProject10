from django.contrib import admin
from .models import projectModel


class projectAdmin(admin.ModelAdmin):
    list_display = ('image', 'For', 'project')


admin.site.register(projectModel, projectAdmin)
# Register your models here.
