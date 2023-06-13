from django.forms import ModelForm
from main.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',    
            'address',      
            'preview_image',
            'date',
            'price',
            'lon',
            'lat',
            'category'      
        ]   