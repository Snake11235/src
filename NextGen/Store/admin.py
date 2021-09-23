from django.contrib import admin

# Register your models here.
from django.contrib import admin
from oscar.core.loading import get_model

Store = get_model('Store', 'Store')


class StoreAdmin(admin.ModelAdmin):
     pass
#
#
admin.site.register(Store, StoreAdmin)