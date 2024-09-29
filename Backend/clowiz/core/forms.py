from django.forms import ModelForm
from .models import Cloth

class NewClothForm(ModelForm):
    class Meta:
        model = Cloth
        fields = ['name', 'image']