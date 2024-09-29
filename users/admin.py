from django.contrib import admin
from .models import Clothes, Accessories, Grooming, Message, Category, ToBuyItem, Tag, Occasion
from .models import Profile

# Register your models here.

admin.site.register(Profile)

admin.site.register(Clothes)
admin.site.register(Accessories)
admin.site.register(Grooming)

admin.site.register(Message)

admin.site.register(Category)
admin.site.register(ToBuyItem)
admin.site.register(Tag)
admin.site.register(Occasion)
