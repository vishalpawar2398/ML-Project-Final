from django.contrib import admin
from .models import usermodel

class userAdmin(admin.ModelAdmin):
    list_display =['Bhk','location','bathroom','balcony','playground','landmark','price_range']

admin.site.register(usermodel,userAdmin)

# Register your models here.
