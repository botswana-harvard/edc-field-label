from django import forms

from .models import MyModel, MyOtherModel, MyLocationModel


class MyModelForm (forms.ModelForm):

    class Meta:
        model = MyModel
        fields = '__all__'


class MyOtherModelForm (forms.ModelForm):

    class Meta:
        model = MyOtherModel
        fields = '__all__'


class MyLocationModelForm (forms.ModelForm):

    class Meta:
        model = MyLocationModel
        fields = '__all__'
