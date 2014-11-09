from django.contrib import admin

# Register your models here.
from fithack.models import *

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(GroupAdmin)
admin.site.register(Data)