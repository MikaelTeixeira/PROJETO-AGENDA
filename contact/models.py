from django.db import models

class Contact(models.Model):
    '''This class represents a contact that will be saved in the database. These fields will be used to create the contacts, and will exist in every contact.'''
  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank= True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, blank= True, null= True)
    show = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
        
class Category(models.Model):

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    '''This class is another table in Database that will be used to group a number of contacts into their proper contexts. '''
    name = models.CharField(max_length=50, unique=True, null=False)
    def __str__(self) -> str:
        return f'{self.name}'