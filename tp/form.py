from django import forms
# from . import script
from django.core.exceptions import ValidationError
class PostForm(forms.Form):
    # p1 = forms.ChoiceField(choices=enumerate(script.choices),label='Player 1')
    # p2 = forms.ChoiceField(choices=enumerate(script.choices),label='Player 2',required=False)
    # x = forms.IntegerField(required=False)
    # y = forms.IntegerField(help_text='Set to 70 if unknown',required=False)
    # z = forms.IntegerField(required=False)
    # players = script.players
    
    # def clean(self):
    #     cleaned_data = super(PostForm, self).clean()
    #     p2 = cleaned_data.get("p2")
    #     cordsx = cleaned_data.get("x")
    #     cordsy = cleaned_data.get("y")
    #     cordsz = cleaned_data.get("z")
    #     if p2 and (cordsx or cordsy or cordsz): # both were entered
    #         raise forms.ValidationError("Enter either co-ords or player 2 name")
    #     elif not p2 and not (cordsx or cordsy or cordsz): # neither were entered
    #         raise forms.ValidationError("You must enter either co-ords or player 2 name")
        
    #     return cleaned_data
    
    
    arg1 = forms.CharField(max_length=50,strip=True)
    arg2 = forms.CharField(max_length=50,strip=True,empty_value='282 90 1163',required=False)

# pl=script.players