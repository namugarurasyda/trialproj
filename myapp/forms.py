from django.forms import ModelForm
from .models import Room

class RoomForm():
    class Meta:
        model = Room
        Fields = '__all__'