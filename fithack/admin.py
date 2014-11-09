from django.contrib import admin
from models import Member, Group, GroupAdmin, Data

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(GroupAdmin)
admin.site.register(Data)