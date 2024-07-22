from django import forms
from .models import WishList

class FoodSearchForm(forms.Form):
    name = forms.CharField(label='輸入食品名稱', max_length=100)

class WishListForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ['name']
