from django import forms

from .models import MyModel, MyLocationModel


class MyModelForm (forms.ModelForm):

    class Meta:
        model = MyModel
        fields = '__all__'


class MyLocationModelForm (forms.ModelForm):

    class Meta:
        model = MyLocationModel
        fields = '__all__'
