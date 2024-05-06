from django.contrib import admin
from .models import Services ,Make_Order ,Doctor , Price , Category , Gallery
# Register your models here.
admin.site.register(Services)

admin.site.register(Make_Order)
admin.site.register(Doctor)
admin.site.register(Price)
admin.site.register(Category)
admin.site.register(Gallery)




