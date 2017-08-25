from django import forms

class BuildOrderForm(forms.Form):
    # get every building
    # build integer field for each building...

    farms = forms.IntegerField(label='Farms', initial=0)
    mills = forms.IntegerField(label='Mills', initial=0)
    houses = forms.IntegerField(label='Houses', initial=0)
