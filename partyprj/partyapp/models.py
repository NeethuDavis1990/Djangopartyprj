from django.db import models

# Create your models here.
class Locationtypemodel(models.Model):
    Locationid=models.IntegerField(auto_created=True,primary_key=True)
    Locationtype=models.CharField(max_length=100,verbose_name="Location")
    def __str__(self):
        return self.Locationtype

class Venumastermodel(models.Model):
    Venuid=models.IntegerField(auto_created=True,primary_key=True)
    Locationtype=models.ForeignKey(Locationtypemodel,on_delete=models.PROTECT,blank=True)
    Venu=models.CharField(max_length=100,verbose_name="Venu")
    def __str__(self):
        return self.Venu

class Menupreferencemastermodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Menupreference=models.CharField(max_length=100,verbose_name="Menu Preference")
    def __str__(self):
        return self.Menupreference

class Gamesmastermodel(models.Model):
    Gameid=models.IntegerField(auto_created=True,primary_key=True)
    Game=models.CharField(max_length=100,verbose_name="Game Name")
    Gametype=models.CharField(max_length=50,verbose_name="Game Type",null=True,blank=True)
    Description=models.TextField(max_length=500,verbose_name="Description")
    Maxparticipants=models.IntegerField(verbose_name="Max Participants")
    Minparticipants=models.IntegerField(verbose_name="Min Participants")
    Locationtype=models.ForeignKey(Locationtypemodel,on_delete=models.PROTECT,blank=True)
    def __str__(self):
        return self.Game

class Inviteesmastermodel(models.Model):
    Invittesid=models.IntegerField(auto_created=True,primary_key=True)
    Inviteename=models.CharField(max_length=100,verbose_name="Name")
    Phonenumber=models.CharField(max_length=100,verbose_name="Phone No")
    Whatsapp=models.CharField(max_length=100,verbose_name="Whatsapp")
    Address=models.CharField(max_length=250,verbose_name="Address")
    Email=models.CharField(max_length=100,verbose_name="Email")
    Gender=models.CharField(max_length=15,verbose_name="Gender")
    Adultorkid=models.CharField(max_length=100,verbose_name="Adult/Kid")
    Menupreference=models.ForeignKey(Menupreferencemastermodel,on_delete=models.PROTECT,blank=True)
    def __str__(self):
        return self.Inviteename
    

class Menucategorymodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Category=models.CharField(max_length=100,verbose_name="Category")
    def __str__(self):
        return self.Category

class Areamastermodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Area=models.CharField(max_length=100,verbose_name="Area Type")
    def __str__(self):
        return self.Area


class Menumastermodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Menucategory=models.ForeignKey(Menucategorymodel,on_delete=models.PROTECT,blank=True)
    Menupreference=models.ForeignKey(Menupreferencemastermodel,on_delete=models.PROTECT,blank=True)
    Area=models.ForeignKey(Areamastermodel,on_delete=models.PROTECT,blank=True)
    Menuname=models.CharField(max_length=100,verbose_name="Menu")
    def __str__(self):
        return self.Menuname


class Partymastermodel(models.Model):
    Partyid=models.IntegerField(auto_created=True,primary_key=True)
    Partyname=models.CharField(max_length=100,verbose_name="Party Name")
    Venue=models.ForeignKey(Venumastermodel,on_delete=models.PROTECT,blank=True)
    Date=models.DateField(verbose_name="Date of Party")
    Time=models.DecimalField(decimal_places=2,max_digits=4,verbose_name="Time")
    Attendeesno=models.IntegerField(verbose_name="Attendees No")
    Locationtype=models.ForeignKey(Locationtypemodel,on_delete=models.PROTECT,blank=True)
    Menupreference=models.ForeignKey(Menupreferencemastermodel,on_delete=models.PROTECT,blank=True)
    PartyInout=models.CharField(max_length=100,verbose_name="Party In(food)")
    Game=models.ManyToManyField(Gamesmastermodel,through="Partygamebridgemodel",
    related_name="Partymastermodel")
    Invitees=models.ManyToManyField(Inviteesmastermodel,through="Partyinviteesbridgemodel",
    related_name="Partymastermodel")
    Menu=models.ManyToManyField(Menumastermodel,through="Partymenubridgemodel",
    related_name="Partymastermodel")
    def __str__(self):
        return self.Partyname


class Partygamebridgemodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Party=models.ForeignKey(Partymastermodel,on_delete=models.PROTECT,blank=True,
    related_name="party_game_bridge_model",null=True)
    Game=models.ForeignKey(Gamesmastermodel,on_delete=models.PROTECT,blank=True,
    related_name="party_game_bridge_model",null=True)
    def __str__(self):
        return f"{self.Party} {self.Game}"

class Partyinviteesbridgemodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Party=models.ForeignKey(Partymastermodel,on_delete=models.PROTECT,blank=True,
    related_name="party_invitees_bridge_model",null=True)
    Invitees=models.ForeignKey(Inviteesmastermodel,on_delete=models.PROTECT,blank=True,
    related_name="party_invitees_bridge_model",null=True)
    def __str__(self):
        return f"{self.Party} {self.Invitees}"



class Partymenubridgemodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Party=models.ForeignKey(Partymastermodel,on_delete=models.PROTECT,blank=True,
    related_name="party_menu_bridge_model",null=True)
    Menu=models.ForeignKey(Menumastermodel,on_delete=models.PROTECT,blank=True,
    related_name="party_menu_bridge_model",null=True)
    def __str__(self):
        return f"{self.Party} {self.Menu}"

class Bringaplatemodel(models.Model):
    Id=models.IntegerField(auto_created=True,primary_key=True)
    Party=models.ForeignKey(Partymastermodel,on_delete=models.PROTECT,blank=True)
    Invitees=models.ForeignKey(Inviteesmastermodel,on_delete=models.PROTECT,blank=True)
    Menu=models.ForeignKey(Menumastermodel,on_delete=models.PROTECT,blank=True)
    Quantity=models.IntegerField(verbose_name="Quantity")
    def __str__(self):
        return f" {self.Party} {self.Invitees} {self.Menu} "
