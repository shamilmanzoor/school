from django.contrib import admin
from .models import Person , City , Country,  Purpose , Gender

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Purpose)
admin.site.register(Gender)




