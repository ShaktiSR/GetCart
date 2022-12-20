from django.contrib import admin

from .models import Poll, Category
from .models import product, order
#from .models import User

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']


#Register your model here
#admin.site.register(User)
admin.site.register(Poll)
admin.site.register(order)
admin.site.register(product, AdminProduct)
admin.site.register(Category, AdminCategory)