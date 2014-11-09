from django.contrib import admin
from models import Member, Group, GroupAdmin, Data

<<<<<<< HEAD
=======
# Register your models here.
from fithack.models import *

>>>>>>> f7a7cc28e93b7f34cd5055b1a3b69b832ec061a3
admin.site.register(Member)
admin.site.register(Group)
admin.site.register(GroupAdmin)
admin.site.register(Data)