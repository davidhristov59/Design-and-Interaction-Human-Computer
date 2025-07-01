from django import forms

from CarDealership.models import Car

class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs) # go trgnav self __init__, ne treba 2 pati
        for field_name, field in self.fields.items():
            if not isinstance(field, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Car
        fields = '__all__'
