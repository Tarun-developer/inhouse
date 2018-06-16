# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class PropertySearch(admin.ModelAdmin):
    
    search_fields = ('location', 'budget')

class OwnerSearch(admin.ModelAdmin):
    
    search_fields = ('name', 'propertie')

class ClientSearch(admin.ModelAdmin):
    
    search_fields = ('name',)

admin.site.register(Furnish)
admin.site.register(Apartment)
admin.site.register(BHK)
admin.site.register(Property,PropertySearch)
admin.site.register(OwnerInfo,OwnerSearch)
admin.site.register(Client,ClientSearch)
admin.site.register(ClientReivew)
admin.site.register(Images)
