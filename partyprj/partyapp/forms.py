
from django import forms
from partyapp.models import (Locationtypemodel,Venumastermodel,
Menupreferencemastermodel,Partymastermodel,Gamesmastermodel,Inviteesmastermodel,
Areamastermodel,Menucategorymodel,Menumastermodel,Bringaplatemodel)
from django.forms import  ModelForm

class Locationtypemodelform(ModelForm):
    class Meta:
        model=Locationtypemodel
        exclude=['Locationid']

class Venumastermodelform(ModelForm):
    class Meta:
        model=Venumastermodel
        exclude=['Venuid']
    
class Menupreferencemastermodelform(ModelForm):
    class Meta:
        model=Menupreferencemastermodel
        exclude=['Id']


class Gamesmastermodelform(ModelForm):
    class Meta:
        model=Gamesmastermodel
        exclude=['Gameid']

class Partymastermodelform(ModelForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        mychoices=Gamesmastermodel.objects.all()
        self.fields["Game"]=forms.ModelMultipleChoiceField(queryset=mychoices,widget=forms.SelectMultiple(attrs={'class':'select2','multiple':'multiple'}))
        #choice=Inviteesmastermodel.objects.all()
       # self.fields["Invitees"]=forms.ModelMultipleChoiceField(queryset=choice,widget=forms.SelectMultiple(attrs={'class':'select2','multiple':'multiple'}))
        #self.fields["Invitees"].required=False
        #choice2=Menumastermodel.objects.all()
      # self.fields["Menu"]=forms.ModelMultipleChoiceField(queryset=choice2,widget=forms.SelectMultiple(attrs={'class':'select2','multiple':'multiple'}))
        
    class Meta:
        model=Partymastermodel
        exclude=['Partyid','Invitees','Menu']
        widgets = {"Date": forms.DateInput(attrs={'class':'datepicker'})}

    
class Inviteesmastermodelform(ModelForm):

    Gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female'),('Other','Other')], widget=forms.Select)
    class Meta:
        model=Inviteesmastermodel
        exclude=['Invittesid']

class Areamastermodelform(ModelForm):

    class Meta:
        model=Areamastermodel
        exclude=['Id']

class Menucategorymodelform(ModelForm):
    class Meta:
        model=Menucategorymodel
        exclude=['Id']

class Menumastermodelform(ModelForm):
    class Meta:
        model=Menumastermodel
        exclude=['Id']

    
class Bringaplatemodelform(ModelForm):
    class Meta:
        model=Bringaplatemodel
        exclude=['Id']

class Partymenucomboform(forms.Form):

    
     Category=forms.ModelChoiceField(queryset=Menucategorymodel.objects.all())
     Foodlist=forms.ModelMultipleChoiceField(queryset=Menumastermodel.objects.all(),widget=forms.SelectMultiple(attrs={'class':'select2','multiple':'multiple'}))

    
       