"""partyprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from partyapp import views

urlpatterns = [
    path('',views.Initialfn,name="Initialfn"),
    path('Locationtypecreate',views.Locationtypecreate,name="Locationtypecreate"),
    path('Locationtypelistview',views.Locationtypelistview,name="Locationtypelist"),
    path('Locationeditview/<int:id>',views.Locationeditview,name="Locationtypeedit"),
    path('Venumastercreate',views.Venumastercreate,name="Venumastercreate"),
    path('Venumasterlist',views.Venumasterlist,name="Venumasterlist"),
    path('Venumasteredit/<int:id>',views.Venumasteredit,name="Venumasteredit"),
    path('Menupreferencecreate',views.Menupreferencecreate,name="Menupreferencecreate"),
    path('Menupreferencelist',views.Menupreferencelist,name="Menupreferencelist"),
    path('Menupreferenceedit/<int:id>',views.Menupreferenceedit,name="Menupreferenceedit"),
    path('Partymastermodelcreate',views.Partymastermodelcreate,name="Partymastermodelcreate"),
    path('Partymasterlist',views.Partymasterlist,name="Partymasterlist"),
    path('Partymasteredit/<int:id>',views.Partymasteredit,name="Partymasteredit"),
    path('Gamesmastercreate',views.Gamesmastercreate,name="Gamesmastercreate"),
    path('Gamesmasterlist',views.Gamesmasterlist,name="Gamesmasterlist"),
    path('gamesmasteredit/<int:id>',views.gamesmasteredit,name="gamesmasteredit"),
    path('Inviteesmastercreate',views.Inviteesmastercreate,name="Inviteesmastercreate"),
    path('inviteemasterlist',views.inviteemasterlist,name="inviteemasterlist"),
    path('inviteemasteredit/<int:id>',views.inviteemasteredit,name="inviteemasteredit"),
    path('Areamastermodelcreate',views.Areamastermodelcreate,name="Areamastermodelcreate"),
    path('Areamastermodellist',views.Areamastermodellist,name="Areamastermodellist"),
    path('Areamastermodeledit/<int:id>',views.Areamastermodeledit,name="Areamastermodeledit"),
    path('Menucategorymodelcreate',views.Menucategorymodelcreate,name="Menucategorymodelcreate"),
    path('Menucategorymodellist',views.Menucategorymodellist,name="Menucategorymodellist"),
    path('Menucategoryedit/<int:id>',views.Menucategoryedit,name="Menucategoryedit"),
    path('Menumastermodelcreate',views.Menumastermodelcreate,name="Menumastermodelcreate"),
    path('Menumastermodellist',views.Menumastermodellist,name="Menumastermodellist"),
    path('Menumastermodeledit/<int:id>',views.Menumastermodeledit,name="Menumastermodeledit"),
    path('Bringaplatemodelcreate',views.Bringaplatemodelcreate,name="Bringaplatemodelcreate"),
    path('Bringaplatemodellist',views.Bringaplatemodellist,name="Bringaplatemodellist"),
    path('Bringaplatemodeledit/<int:id>',views.Bringaplatemodeledit,name="Bringaplatemodeledit"),
    path('Inviteeslistinorderwithparty',views.Inviteeslistinorderwithparty,name="Inviteeslistinorderwithparty"),
    path('Gamelistinorderwithparty',views.Gamelistinorderwithparty,name="Gamelistinorderwithparty"),
    path('Partylistnewview',views.Partylistnewview,name="Partylistnewview"),
    path('Partygamelistfrombridgetable/<str:Partyname>',views.Partygamelistfrombridgetable,name="Partygamelistfrombridgetable"),
    path('Partyinviteelistfrombridgetable/<str:Partyname>',views.Partyinviteelistfrombridgetable,name="Partyinviteelistfrombridgetable"),
    path('Partywithoutwelcomedrink',views.Partywithoutwelcomedrink,name="Partywithoutwelcomedrink"),
    path('Listgamesdoesnotassignedtoparty',views.Listgamesdoesnotassignedtoparty,name="Listgamesdoesnotassignedtoparty"),
    path('Inviteeandpartylist_view',views.Inviteeandpartylist_view,name="Inviteeandpartylist_view"),
    path('Partiesandnoofgameslist_view',views.Partiesandnoofgameslist_view,name="Partiesandnoofgameslist_view"),
    path('Partiesandnoofmenusassigned_view',views.Partiesandnoofmenusassigned_view,name="Partiesandnoofmenusassigned"),
    path('Pagination_practise',views.Pagination_practise,name="Pagination_practise"),
    path('admin/', admin.site.urls),
    path('Jquery_pagination_view1/<int:currentpage>',views.Jquery_pagination_view1,name="Jquery_pagination_view1"),
    path('Jquery_pagination_view',views.Jquery_pagination_view,name="Jquery_pagination_view"),
    path('Partyinviteelist/<int:id>',views.Partyinviteelist,name="Partyinviteelist"),
    path('Party_menu_combodetails/<int:id>',views.Party_menu_combodetails,name="Party_menu_combodetails"),
    path('Partynameduplicatevalidation',views.Partynameduplicatevalidation,name="Partynameduplicatevalidation"),
    path('Getfoodlistbasedoncategoryusingajax',views.Getfoodlistbasedoncategoryusingajax,name="Getfoodlistbasedoncategoryusingajax"),
]
