from django.contrib import admin
from contact.models import Contact_model


class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_details')


admin.site.register(Contact_model, contactAdmin)
# Register your models here.
