from django.contrib import admin

from . models import Product,Review,Callback,mailstore


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock']
    list_editable = ['price','stock']


admin.site.register(Product,ProductAdmin)

class Revviewad(admin.ModelAdmin):
    list_display = ['name','desc']



admin.site.register(Review,Revviewad)


class Callbackhg(admin.ModelAdmin):
    list_display = ['name','message']



admin.site.register(Callback,Callbackhg)

class maily(admin.ModelAdmin):
    list_display = ['email']



admin.site.register(mailstore,maily)