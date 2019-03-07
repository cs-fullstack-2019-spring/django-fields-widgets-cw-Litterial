from django import forms
from .models import HeroApplication

MoneyPower=(('1','Rich'),('2','Super Powers'))
Side=(('1','Good'),('2','Kinda good'),('3','Neutral'),('4','A little evil'),('5','Evil'))
Abilities=(('1','Flight'),('2','Speed'),('3','Invisibility'),('4','Telekenetics'),('5','Healing'),('6','Other'))
class HeroForm(forms.ModelForm):
    class Meta:
        model=HeroApplication
        fields='__all__'
        labels={
            'city':"City or origin",
            'powers':'Are you rich or do you have Super Powers?',
            'power_type':'If you have Super Powers, which ones?',
            'alignment':'Which of the following are you?',
            'example':'Give us three examples of when you used your super hero abilities.'
        }
        widgets={
            'powers':forms.RadioSelect(choices=MoneyPower),
            'alignment':forms.RadioSelect(choices=Side),
            'example':forms.Textarea,
            'power_type':forms.CheckboxSelectMultiple(choices=Abilities)
        }