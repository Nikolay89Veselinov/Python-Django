from django import forms

from .models import OpenStreetMaps


class OpenStreetMapsForm(forms.ModelForm):

    class Meta:
        model = OpenStreetMaps
        fields = ('location', 'location_lat', 'location_lon', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget = forms.TextInput()
        self.fields['location'].widget.attrs['class'] = 'osmfield'
        self.fields['location'].widget.attrs['data-lat-field'] = 'location_lat'
        self.fields['location'].widget.attrs['data-lon-field'] = 'location_lon'
