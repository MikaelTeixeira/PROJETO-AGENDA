from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Contact)

class Contact_admin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone','email', 'show',
    list_display_links = ('id',)
    list_editable = 'first_name','last_name', 'show',
    list_per_page = 10

@admin.register(models.Category)
class Category_admin(admin.ModelAdmin):
    list_display= ('name',)
    ordering= ('-id',)