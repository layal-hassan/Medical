from django import forms

from .models import Make_Order

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Make_Order
        fields = ('name', 'Email' , 'comment')

