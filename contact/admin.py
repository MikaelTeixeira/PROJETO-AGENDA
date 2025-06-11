from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Contact)
class Contact_admin(admin.ModelAdmin):
    list_display = 'first_name','last_name','phone','email'
