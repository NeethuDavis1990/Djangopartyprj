from django.contrib import admin
from partyapp.models import (Locationtypemodel,Menucategorymodel,Menumastermodel,
Menupreferencemastermodel,Areamastermodel,Venumastermodel,Partymastermodel,Inviteesmastermodel,
Gamesmastermodel,Partymenubridgemodel,Partygamebridgemodel,Partyinviteesbridgemodel,
Bringaplatemodel)

# Register your models here.
admin.site.register(Locationtypemodel)
admin.site.register(Menucategorymodel)
admin.site.register(Menumastermodel)
admin.site.register(Menupreferencemastermodel)
admin.site.register(Areamastermodel)
admin.site.register(Venumastermodel)
admin.site.register(Partymastermodel)
admin.site.register(Inviteesmastermodel)
admin.site.register(Gamesmastermodel)
admin.site.register(Partyinviteesbridgemodel)
admin.site.register(Partygamebridgemodel)
admin.site.register(Partymenubridgemodel)
admin.site.register(Bringaplatemodel)