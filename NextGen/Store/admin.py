from django.contrib import admin

# Register your models here.
from django.contrib import admin
from oscar.core.loading import get_model
from .models import Slider,Logo
Store = get_model('Store', 'Store')
#slider = get_model('Slider','Slider')

class StoreAdmin(admin.ModelAdmin):
     pass
#
#
#class SliderAdmin(admin.ModelAdmin):
#     pass
admin.site.register(Store, StoreAdmin)
admin.site.register(Slider)
admin.site.register(Logo)