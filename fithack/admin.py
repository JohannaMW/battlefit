from django.contrib import admin
<<<<<<< HEAD
from models import Member, Group, GroupAdmin, Data
=======
from fithack.models import *
>>>>>>> 65b8134f471f17c3791905cd17a4bae83f43c13f

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(GroupAdmin)
admin.site.register(Data)