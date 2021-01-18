from django.contrib import admin
from .models import Contact, cardimage, contacts, about, social

# Register your models here.
admin.site.register(Contact)
admin.site.register(cardimage)
admin.site.register(contacts)
admin.site.register(about)
admin.site.register(social)
