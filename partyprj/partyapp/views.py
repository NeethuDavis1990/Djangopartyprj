from functools import partial


from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count,Max 
from partyapp.models import (Locationtypemodel,Venumastermodel,
Menupreferencemastermodel,Partymastermodel,Gamesmastermodel,Inviteesmastermodel,
Areamastermodel,Menucategorymodel,Menumastermodel,Bringaplatemodel,
Partyinviteesbridgemodel,Partygamebridgemodel,Partymenubridgemodel)
from partyapp.forms import (Locationtypemodelform,Venumastermodelform,
Menupreferencemastermodelform,Partymastermodelform,Gamesmastermodelform,
Inviteesmastermodelform,Areamastermodelform,Menucategorymodelform,
Menumastermodelform,Bringaplatemodelform,Partymenucomboform)
from django.core.paginator import Paginator
import math

# Create your views here.

def Initialfn(request):
    return render(request,'partyapp/base.html')

def Locationtypecreate(request):
    Locationinst=Locationtypemodelform()
    context={'Locationhtml': Locationinst}
    if request.method=="GET":
        return render(request,'partyapp/locationtypecreate.html',context)
    elif request.method=="POST":
        Locationobj=Locationtypemodelform(request.POST)
        if Locationobj.is_valid():
            Locationobj.save()
            Locationinst=Locationtypemodelform()
            context={'Locationhtml':Locationinst}
            return render(request,'partyapp/locationtypecreate.html',context)
        else:
            context={'error':"error"}
            return render(request,'partyapp/locationtypecreate.html',context)

def Locationtypelistview(request):
    if request.method=="GET":
        Locationinst=Locationtypemodel.objects.all()
        context={'Locationlist':Locationinst}
        return render(request,'partyapp/locationtypelist.html',context)

def Locationeditview(request,id=None):
    Locationiddet=Locationtypemodel.objects.get(Locationid=id)
    Locationobj=Locationtypemodelform(instance=Locationiddet)
    if request.method=="GET":
        context={'Locationhtml': Locationobj}
        return render(request,'partyapp/locationtypecreate.html',context)
    elif request.method =="POST":
        Locationedit=Locationtypemodelform(request.POST,instance=Locationiddet)
        Locationedit.save()
        context={'Locationhtml':Locationedit}
        return render(request,'partyapp/locationtypecreate.html',context)

def Venumastercreate(request):
    if request.method=="GET":
        Venumasterinst=Venumastermodelform()
        context={'venuhtml':Venumasterinst}
        return render(request,'partyapp/venumastercreate.html',context)
    elif request.method=="POST":
        Venumasterobj=Venumastermodelform(request.POST)
        if Venumasterobj.is_valid():
            Venumasterobj.save()
            Venumasterinst=Venumastermodelform()
            context={'venuhtml':Venumasterinst}
            return render(request,'partyapp/venumastercreate.html',context)
        else:
            context={'error':"error"}
            return render(request,'partyapp/venumastercreate.html',context)


def Venumasterlist(request):
    if request.method=="GET":
        Venuinstlist=Venumastermodel.objects.all()
        context={'venulist':Venuinstlist}
        return render(request,'partyapp/venumasterlist.html',context)

def Venumasteredit(request,id=None):
     Venuinst=Venumastermodel.objects.get(Venuid=id)
     Venuobj=Venumastermodelform(instance=Venuinst)
     if request.method=="GET":
         context={'venuhtml':Venuobj}
         return render(request,'partyapp/venumastercreate.html',context)
     elif request.method=="POST":
         Venueditsave=Venumastermodelform(request.POST,instance=Venuinst)
         Venueditsave.save()
         context={'venuhtml':Venueditsave}
         return render(request,'partyapp/venumastercreate.html',context)


def Menupreferencecreate(request):
    if request.method=="GET":
        menuobj=Menupreferencemastermodelform()
        context={'menuhtml':menuobj}
        return render(request,'partyapp/menupreferencecreate.html',context)
    elif request.method=="POST":
        menuinst=Menupreferencemastermodelform(request.POST)
        if menuinst.is_valid():
            menuinst.save()
            menuobj=Menupreferencemastermodelform()
            context={'menuhtml':menuobj}
            return render(request,'partyapp/menupreferencecreate.html',context)
        else:
            context={'error':"error"}
            return render(request,'partyapp/menupreferencecreate.html',context)

def Menupreferencelist(request):
    if request.method=="GET":
        Menuinst=Menupreferencemastermodel.objects.all()
        context={'menulist':Menuinst}
        return render(request,'partyapp/menupreferencelist.html',context)

def Menupreferenceedit(request,id=None):
    menuinst=Menupreferencemastermodel.objects.get(Id=id)
    menuobj=Menupreferencemastermodelform(instance=menuinst)
    if request.method=="GET":
        context={'menuhtml':menuobj}
        return render(request,'partyapp/menupreferencecreate.html',context)
    elif request.method=="POST":
        menueditsave=Menupreferencemastermodelform(request.POST,instance=menuinst)
        menueditsave.save()
        context={'menuhtml':menueditsave}
        return render(request,'partyapp/menupreferencecreate.html',context)



def Gamesmastercreate(request):
    if request.method=="GET":
        Gamesinst=Gamesmastermodelform()
        context={'gameshtml':Gamesinst}
        return render(request,'partyapp/gamesmastercreate.html',context)
    elif request.method=="POST":
        Gamesobj=Gamesmastermodelform(request.POST)
        if Gamesobj.is_valid():
            Gamesobj.save()
            Gamesinst=Gamesmastermodelform()
            context={'gameshtml':Gamesinst}
            return render(request,'partyapp/gamesmastercreate.html',context)

def Gamesmasterlist(request):
    if request.method=="GET":
        Gamesinst=Gamesmastermodel.objects.all()
        context={'gameslist': Gamesinst}
        return render(request,'partyapp/gamesmasterlist.html',context)

def gamesmasteredit(request,id=None):
    Gameinst=Gamesmastermodel.objects.get(Gameid=id)
    Gameobj=Gamesmastermodelform(instance=Gameinst)
    if request.method=="GET":
        context={'gameshtml':Gameobj}
        return render(request,'partyapp/gamesmastercreate.html',context)
    elif request.method=="POST":
        Gameeditsave=Gamesmastermodelform(request.POST,instance=Gameinst)
        Gameeditsave.save()
        context={'gameshtml':Gameeditsave}
        return render(request,'partyapp/gamesmastercreate.html',context)


def Partymastermodelcreate(request):
    if request.method=="GET":
        partyinst=Partymastermodelform()
        context={'partyhtml':partyinst}
        return render(request,'partyapp/partymastercreate.html',context)
    elif request.method=="POST":
        partyobj=Partymastermodelform(request.POST)
        print(partyobj.errors)
        if partyobj.is_valid():
            todolist=partyobj.save(commit=False)
            partylastobj=Partymastermodel.objects.last()
            if partylastobj==None:
              idincrement=1
            else:
              idincrement=(partylastobj.Partyid + 1)
            todolist.Partyid=idincrement
            todolist.save()
            partyobj.save_m2m()
            partyinst=Partymastermodelform()
            context={'partyhtml':partyinst}
            return render(request,'partyapp/partymastercreate.html',context)
        else:
            context={'error':"errror"}
            return render(request,'partyapp/partymastercreate.html',context)

def Partymasterlist(request):
    if request.method=="GET":
       partylistobj=Partymastermodel.objects.all()
       context={'partylist':partylistobj}
       return render(request,'partyapp/partymasterlist.html',context)
    
def Partymasteredit(request,id=None):
    Partyinst=Partymastermodel.objects.get(Partyid=id)
    Partyobj=Partymastermodelform(instance=Partyinst)
    if request.method=="GET":
        context={'partyhtml': Partyobj}
        return render(request,'partyapp/partymastercreate.html',context)
    elif request.method=="POST":
        Partyeditedobj=Partymastermodelform(request.POST,instance=Partyinst)
        Partyeditedobj.save()
        context={'partyhtml': Partyeditedobj}
        return render(request,'partyapp/partymastercreate.html',context)
        
def Partyinviteelist(request,id=None):
    if request.method=="GET":
        partyinst=Partymastermodel.objects.get(Partyid=id)
        partylist=Partyinviteesbridgemodel.objects.filter(Party=partyinst)
        print(partylist.values_list('Invitees'))
        context={'inviteelist':partylist,"PartyId":id}
        return render(request,'partyapp/partyinviteelist.html',context)
    elif request.method=="POST":
        partyid=request.POST.get('id')
        partyinst=Partymastermodel.objects.get(Partyid=partyid)
        inviteename=request.POST.get('Invitee_name')
        inviteeobj=Inviteesmastermodel.objects.get(Inviteename__exact=inviteename)
        partyinviteeobj=Partyinviteesbridgemodel()
        partyinviteeobj.Invitees=inviteeobj
        partyinviteeobj.Party=partyinst
        partyinviteeobj.save()        
       
        partyinst=Partymastermodel.objects.get(Partyid=id)
        partylist=Partyinviteesbridgemodel.objects.filter(Party=partyinst)
        print(partylist.values_list('Invitees'))
        context={'inviteelist':partylist}
        return render(request,'partyapp/partyinviteelist.html',context)


      

def Inviteesmastercreate(request):
    if request.method=="GET":
        Inviteemdl=Inviteesmastermodelform()
        context={'inviteehtml': Inviteemdl}
        return render(request,'partyapp/inviteemastercreate.html',context)
    elif request.method=="POST":
        Inviteeobj=Inviteesmastermodelform(request.POST)
        if Inviteeobj.is_valid():
            Inviteeobj.save()
            Inviteemdl=Inviteesmastermodelform()
            context={'inviteehtml': Inviteemdl}
            return render(request,'partyapp/inviteemastercreate.html',context)
        else:
            context={'error':"error"}
            return render(request,'partyapp/inviteemastercreate.html',context)

def inviteemasterlist(request):
    if request.method=="GET":
        Inviteeinst=Inviteesmastermodel.objects.all()
        context={'inviteelist':Inviteeinst}
        return render(request,'partyapp/inviteemasterlist.html',context)

def inviteemasteredit(request,id=None):
    inviteeinst=Inviteesmastermodel.objects.get(Invittesid=id)
    inviteeobj=Inviteesmastermodelform(instance=inviteeinst)
    if request.method=="GET":
        context={'inviteehtml': inviteeobj}
        return render(request,'partyapp/inviteemastercreate.html',context)
    elif request.method=="POST":
        inviteeeditnew=Inviteesmastermodelform(request.POST,instance=inviteeinst)
        inviteeeditnew.save()
        context={'inviteehtml':inviteeeditnew}
        return render(request,'partyapp/inviteemastercreate.html',context)

def Areamastermodelcreate(request):
    if request.method=="GET":
        Areainst=Areamastermodelform()
        context={'areahtml': Areainst}
        return render(request,'partyapp/areamastermodelcreate.html',context)
    elif request.method=="POST":
        Areaobj=Areamastermodelform(request.POST)
        if Areaobj.is_valid():
            Areaobj.save()
            Areainst=Areamastermodelform()
            context={'areahtml': Areainst}
            return render(request,'partyapp/areamastermodelcreate.html',context)
        else:
            context={'error':"errror"}
            return render(request,'partyapp/areamastermodelcreate.html',context)
       
def Areamastermodellist(request):
    if request.method=="GET":
        Areainst=Areamastermodel.objects.all()
        context={'arealist':Areainst}
        return render(request,'partyapp/areamastermodellist.html',context)

def Areamastermodeledit(request,id=None):
    areainst=Areamastermodel.objects.get(Id=id)
    areaobj=Areamastermodelform(instance=areainst)
    if request.method=="GET":
        context={'areahtml':areaobj}
        return render(request,'partyapp/areamastermodelcreate.html',context)
    elif request.method=="POST":
        areaeditsave=Areamastermodelform(request.POST,instance=areainst)
        areaeditsave.save()
        context={'areahtml':areaeditsave}
        return render(request,'partyapp/areamastermodelcreate.html',context)


def Menucategorymodelcreate(request):
    if request.method=="GET":
        menuinst=Menucategorymodelform()
        context={'menucategoryhtml':menuinst}
        return render(request,'partyapp/menucategorycreate.html',context)
    elif request.method=="POST":
        menuobj=Menucategorymodelform(request.POST)
        if menuobj.is_valid():
            menuobj.save()
            menuinst=Menucategorymodelform()
            context={'menucategoryhtml':menuinst}
            return render(request,'partyapp/menucategorycreate.html',context)
        else:
            context={'error':"errror"}
            return render(request,'partyapp/menucategorycreate.html',context)

def Menucategorymodellist(request):
    if request.method=="GET":
        menuinst=Menucategorymodel.objects.all() 
        context={'menulist':menuinst}   
        return render(request,'partyapp/menucategorylist.html',context)

def Menucategoryedit(request,id=None):
    menuinst=Menucategorymodel.objects.get(Id=id)
    menuobj=Menucategorymodelform(instance=menuinst)
    if request.method=="GET":
        context={'menucategoryhtml':menuobj}
        return render(request,'partyapp/menucategorycreate.html',context)
    elif request.method=="POST":
        menueditnew=Menucategorymodelform(request.POST,instance=menuinst)
        menueditnew.save()
        context={'menucategoryhtml':menueditnew}
        return render(request,'partyapp/menucategorycreate.html',context)
    
def Menumastermodelcreate(request):
    if request.method=="GET":
        menuinst=Menumastermodelform()
        context={'menumasterhtml':menuinst}
        return render(request,'partyapp/menumastercreate.html',context)
    elif request.method=="POST":
        menuobj=Menumastermodelform(request.POST)
        if menuobj.is_valid():
            menuobj.save()
            menuinst=Menumastermodelform()
            context={'menumasterhtml':menuinst}
            return render(request,'partyapp/menumastercreate.html',context)
        else:
            context={'error':"error"}
            return render(request,'partyapp/menumastercreate.html',context)

def Menumastermodellist(request):
    if request.method=="GET":
        menuinst=Menumastermodel.objects.all()
        context={'menulist':menuinst}
        return render(request,'partyapp/menumasterlist.html',context)

def Menumastermodeledit(request,id=None):
    menuinst=Menumastermodel.objects.get(Id=id)
    menuobj=Menumastermodelform(instance=menuinst)
    if request.method=="GET":
        context={'menumasterhtml': menuobj }
        return render(request,'partyapp/menumastercreate.html',context)
    elif request.method=="POST":
        menueditsave=Menumastermodelform(request.POST,instance=menuinst)
        menueditsave.save()
        context={'menumasterhtml':menueditsave}
        return render(request,'partyapp/menumastercreate.html',context)
        

def Bringaplatemodelcreate(request):
    if request.method=="GET":
        bringinst=Bringaplatemodelform()
        context={'bringhtml': bringinst}
        return render(request,'partyapp/bringaplatecreate.html',context)
    elif request.method=="POST":
        bringobj=Bringaplatemodelform(request.POST)
        if bringobj.is_valid():
            bringobj.save()
            bringinst=Bringaplatemodelform()
            context={'bringhtml': bringinst}
            return render(request,'partyapp/bringaplatecreate.html',context)
        else:
            context={'error':"error"}
            return render(request,'partyapp/bringaplatecreate.html',context)
        
            
def Bringaplatemodellist(request):
    if request.method=="GET":
        Bringaplatelistinst=Bringaplatemodel.objects.all()
        context={'bringaplatelist':Bringaplatelistinst}
        return render(request,'partyapp/bringaplatelist.html',context)

def Bringaplatemodeledit(request,id=None):
    bringinst=Bringaplatemodel.objects.get(Id=id)
    bringaplatgeobj=Bringaplatemodelform(instance=bringinst)
    if request.method=="GET":
        context={'bringhtml':bringaplatgeobj}
        return render(request,'partyapp/bringaplatecreate.html',context)
    elif request.method=="POST":
        bringeditsave=Bringaplatemodelform(request.POST,instance=bringinst)
        bringeditsave.save()
        context={'bringhtml':bringeditsave}
        return render(request,'partyapp/bringaplatecreate.html',context)


def Inviteeslistinorderwithparty(request):
   
    inviteeinst=Inviteesmastermodel.objects.get(Inviteename="Meera")
    partyinviteequery=Partyinviteesbridgemodel.objects.all().order_by("Party__Partyname").exclude(Invitees=inviteeinst)
    print(partyinviteequery)
    context={'partylist':partyinviteequery}
    return render(request,'partyapp/ormpractise.html',context)

def Gamelistinorderwithparty(request):
    gameinst=Gamesmastermodel.objects.get(Game='Kahoot')
    partygamequery=Partygamebridgemodel.objects.filter(Game=gameinst)
    print(partygamequery)
    context={'list':partygamequery}
    return render(request,'partyapp/gamelistparty.html',context)

def Partylistnewview(request):
    partyquery=Partymastermodel.objects.all()
    context={'partylist':partyquery}
    return render(request,'partyapp/partylistnewview.html',context)

def Partygamelistfrombridgetable(request,Partyname=None):
    partyquery=Partymastermodel.objects.all()
    partyinst=Partymastermodel.objects.get(Partyname=Partyname)
    partygamequery=Partygamebridgemodel.objects.filter(Party=partyinst)
    print(partygamequery)
    context={'partylist':partyquery,'gamelist':partygamequery}
    return render(request,'partyapp/partygamelistview.html',context)

def Partyinviteelistfrombridgetable(request,Partyname=None):
    partyquery=Partymastermodel.objects.all()
    partyinst=Partymastermodel.objects.get(Partyname=Partyname)
    partyinviteequery=Partyinviteesbridgemodel.objects.filter(Party=partyinst)
    context={'partylist':partyquery,'inviteelist':partyinviteequery}
    return render(request,'partyapp/partyinviteelistview.html',context)

def Partywithoutwelcomedrink(request):
    Menuinst=Menucategorymodel.objects.get(Category="Welcome Drink")
    partyqueryset=Partymastermodel.objects.exclude(Menu__Menucategory__Category=Menuinst.Category)
    print(partyqueryset)
    print(Menuinst)
    context={'menulist':partyqueryset}
    return render(request,'partyapp/partywithoutwelcomedrink.html',context)

def Listgamesdoesnotassignedtoparty(request):
    #partygamequeryset=Partygamebridgemodel.objects.all().values_list('Game__Gameid')
    #gamequeryset=Gamesmastermodel.objects.exclude(Gameid__in=partygamequeryset)
    
    #anootateset=Partymastermodel.objects.annotate(inviteeno=Count('Invitees'))
    # print(anootateset[2].Partyname)
    # print(anootateset[2].inviteeno)
    #print(anootateset.order_by('-inviteeno')[:1])
    
    #gameanotateset=Partymastermodel.objects.annotate(game_count=Count("Game"))
    #print(gameanotateset[1])
    #print(gameanotateset[1].game_count)
    
    # menuprefinst=Menupreferencemastermodel.objects.get(Menupreference="Veg")
    # inviteequerset=Inviteesmastermodel.objects.filter(Menupreference__Menupreference=menuprefinst)
    # partyinst=Partymastermodel.objects.get(Partyname="Xmas Eve2020")
    # partyinviteequeryset=Partyinviteesbridgemodel.objects.filter(Party__Partyname=partyinst)
    # print(inviteequerset)    
    # print(partyinviteequeryset) 
    # itemlist=[]
    # for item in inviteequerset:
    #     for item1 in partyinviteequeryset:
    #       if item.Inviteename==item1.Invitees.Inviteename:
    #         itemlist.append(item)
    # print(itemlist)  

    # areainst=Areamastermodel.objects.get(Area="Indian")
    # catinst=Menucategorymodel.objects.get(Category="Dessert")
    # meniqueryset=Menumastermodel.objects.filter(Area__Area=areainst).filter(Menucategory__Category=catinst)
    # print(meniqueryset)
   
    #anootateset=Partymastermodel.objects.annotate(num_invitees=Count('Invitees'))
    #print(anootateset[2].num_invitees)

    # partyinviteequery=Inviteesmastermodel.objects.annotate(party_count=Count('Partymastermodel')).order_by("Inviteename")
    # print(partyinviteequery[0].party_count)
    # print(partyinviteequery[0].Inviteename)
    
   
    
    # partyantset=Partymastermodel.objects.annotate(num_game=Count('Game',distinct=True))
    # #print(len(partyantset))
    # counter=0
    # for item in partyantset:
    #     if item.num_game!=0:
    #         counter=counter+1
    # # no of parties that has game assigned (from bridgetable)
    # partyset=Gamesmastermodel.objects.annotate(num_party=Count('Partymastermodel'))
    # #print(partyset)
    # allpartygamelist=[]
    # for item in partyset:
    #     print(item.num_party)
    #     if counter==item.num_party:
    #         allpartygamelist.append(item)
    # print(allpartygamelist)        

    
    # partyset=Partyinviteesbridgemodel.objects.all().values_list('Party__Partyname').distinct()
    # #print(partyset)
    # partyinviteedet=Partymastermodel.objects.all().values_list('Partyname','Invitees__Inviteename','Invitees__Gender','Invitees__Adultorkid').order_by('Partyname')
    # print(partyinviteedet)


    # invantset=Inviteesmastermodel.objects.annotate(num_party=Count('Partymastermodel'))
    # print(invantset[2].num_party)
    # print(invantset[2].Inviteename)

    
    
	
    invantset=Partymastermodel.objects.filter(Partyname="Onam2020").annotate(num_invitee=Count('Invitees')).values_list('Invitees')
    print(invantset[1].num_invitee)
    #print(invantset[2].Inviteename)
    
       

    gamelist=Partymastermodel.objects.filter(party_game_bridge_model__Game__Game="Kahoot")
    print(gamelist)
        


    

    



    context={'gamelist':"errro"}
    return render(request,'partyapp/Listgamesdoesnotassignedtoparty.html',context)



def Inviteeandpartylist_view(request):
    partyinviteequery=Inviteesmastermodel.objects.annotate(party_count=Count('Partymastermodel'))
    print(partyinviteequery[0].party_count)
    print(partyinviteequery[0].Inviteename)
    context={'list':partyinviteequery}
    return render(request,'partyapp/Inviteeandpartylist.html',context)

def Partiesandnoofgameslist_view(request):
    partygamequery=Partymastermodel.objects.annotate(num_game=Count('Game'))
    print(partygamequery[0].num_game)
    print(partygamequery[0].Partyname)
    context={'list':partygamequery}
    return render(request,'partyapp/Partiesandnoofgameslist.html',context)

def Partiesandnoofmenusassigned_view(request):
    partymenuqueryset=Partymastermodel.objects.annotate(num_menu=Count("Menu"))
    context={'list':partymenuqueryset}
    return render(request,'partyapp/Partiesandnoofmenusassigned.html',context)

def Pagination_practise(request):
    if request.method=="GET":
        page_num = request.GET.get('page',1)
        query = request.GET.get('searchterm','')
    partylist=Partymastermodel.objects.filter(Partyname__contains=query).order_by('Partyid')
    party_paginator=Paginator(partylist,3)
    page = party_paginator.get_page(page_num)   
    print(page.object_list)    
    context = {
    'count' : party_paginator.count,
    'page' : page,
    'searchterm':''
    }

    return render(request,'partyapp/paginationpractise.html',context)


def Jquery_pagination_view(request):

   
    Partylist=Partymastermodel.objects.all().order_by('Partyname')
    party_length=len(Partylist)
    page_size=2
    anchor_loop=int(party_length/page_size)+(party_length%page_size)
    #print(anchor_loop)
    context={'partylist':Partylist,
            'anchorcount':range(anchor_loop)                    
                                      }

    return render(request,'partyapp/jquerypagination.html',context)



def Jquery_pagination_view1(request,currentpage=0):
    page_size=2
    intpagenum=currentpage
    partylen=Partymastermodel.objects.all()
    party_length=len(partylen)
    if currentpage==0:
      startnum=(intpagenum)*2
      endnum=startnum+2
      Partylist=Partymastermodel.objects.all().order_by('Partyname')[startnum:endnum]
      print(currentpage)
    else: 
      print(currentpage)
      startnum=(intpagenum)*2
      endnum=startnum+2

      Partylist= Partymastermodel.objects.all().order_by('Partyname')[startnum:endnum]
    #   Partylist= Partymastermodel.objects.all()[2:6]
    print(Partylist) 
    #party_length=len(Partylist)
    
    anchor_loop=int(party_length/page_size)+(party_length%page_size)
    #print(anchor_loop)
    context={'partylist':Partylist,
            'anchorcount':range(anchor_loop)                    
                                      }

    return render(request,'partyapp/jquerypagination.html',context)
        

def Partynameduplicatevalidation(request):
    Partylist=Partymastermodel.objects.all()
    newpartyname=request.GET.get('argpartyname') 
    newpartyinst=Partymastermodel.objects.get(Partyname=newpartyname)
    if newpartyinst==newpartyname:
          context={'error':"This field exists"}
    else:
          context={'party':newpartyname}
          #return render(request,'partyapp/partymastercreate.html',context)
          return JsonResponse(context,safe=False)

          
   


def Party_menu_combodetails(request,id=None):
    Partyinst=Partymastermodel.objects.get(Partyid=id)
    if request.method=="GET":
     partymenuinst=Partymenucomboform()
     context={'partyinst':Partyinst,'myform':partymenuinst}
     return render(request,'partyapp/Party_menu_combodetails.html',context)
    elif request.method=="POST":
        partyid=id
        Menuids=request.POST.getlist('Foodlist') #name
        print(Menuids)
        partyinst=Partymastermodel.objects.get(Partyid=partyid)
        for item in Menuids:
            menuinst=Menumastermodel.objects.get(Id=item)
            partymenuinst=Partymenubridgemodel()
            partymenuinst.Party=partyinst
            partymenuinst.Menu=menuinst
            partymenuinst.save()
        context={'partyinst':Partyinst,'myform':"msh"}
        return render(request,'partyapp/Party_menu_combodetails.html',context)     
            
    else:
        context={'error':"error"}
        return render(request,'pydateapp/studentcreate.html',context)
           




def Converttodictfoodlist(foodlist):
    returndic={}
    localdic={}
    for item in foodlist:
        localdic["value"]=item.Id
        localdic["text"]=item.Menuname      
        
        returndic[item.Id]=localdic        
        localdic={}
    return returndic

def Getfoodlistbasedoncategoryusingajax(request):
    if request.method=="GET":
        category=request.GET.get("argcategory")
        print(category)
        actinst=Menucategorymodel.objects.get(Id=category)
        foodlist=Menumastermodel.objects.filter(Menucategory__Category=actinst)
        print(foodlist)
        jsonresult=Converttodictfoodlist(foodlist)
        return JsonResponse(jsonresult,safe=False)


def Repeatedvenudateandtimeresponsefn(request):
    if request.method=="GET":
        partytime=request.GET.get('argnewtime')
        partydate=request.GET.get('argnewdate')
        partyvenue=request.GET.get('argnewvenue')
        venuinst=Partymastermodel.objects.get(Venu__Venu=partyvenue)
        print(venuinst)
        





    context={'partyhtml':'partyinst'} 
    return render(request,'partyapp/partymastercreate.html',context)