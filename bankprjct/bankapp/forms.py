from .models import Person, City
from django import forms
from django.forms.widgets import NumberInput
from.models import material
#[(item.material) for item in material.objects.all()]
MATERIAL_CHOICES=(("debitcard","debitcard"),("creditcard","creditcard"),("prepaidcard","prepaidcard"),("cheque","cheque"))
boolChoice= [("male","male"),("female","female"),("other","other")]      
class PersonForm(forms.ModelForm):
    username=forms.CharField()
    name=forms.CharField()
    birthdate=forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    email=forms.EmailField()
    phone=forms.IntegerField()
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=boolChoice)
    address=forms.CharField(widget=forms.Textarea(attrs={'style':'height:5em;width:15em'}))
    material=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=MATERIAL_CHOICES)
    class Meta:
        model = Person
        fields = ('username','name', 'birthdate','email','phone','gender','address','account','material', 'state', 'city')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

        