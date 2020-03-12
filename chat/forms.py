from django import forms
from chat import models


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddRoomForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            self.fields[key].widget.attrs.update({'class': 'form-control'})
            self.fields[key].widget.attrs.update({'placeholder': key})