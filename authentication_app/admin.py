from django.contrib import admin
from authentication_app.models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(CountryLanguage)