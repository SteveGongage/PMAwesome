from django import forms
from properties.models import Property, Lease

class PropForm(forms.ModelForm):
    #name = forms.CharField(label = 'Property Name', max_length=50)

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['name', 'slug', 'addressFull', 'addressShort', 'isMapable', 'mapNotes', 'mapLatitude', 'mapLongitude']


class LeaseForm(forms.ModelForm):

    class Meta:
        model = Lease
        fields = '__all__'
        exclude = [ 'end_dateMoveOut', 'end_actionNotes', 'end_ActionFinal', 'end_ActionFinalDate', 'end_ActionOwner', 'end_ActionOwnerDate', 'end_ActionTenants', 'end_ActionTenantsDate', 'end_moveOutNotes', 'start_moveInNotes', 'start_dateLeaseSigned', 'start_dateMoveIn', 'start_isRenewal', 'isActive', 'prop']
