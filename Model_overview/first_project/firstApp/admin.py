from django.contrib import admin
from firstApp.models import AccessRecord,Webpage,Topic
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)