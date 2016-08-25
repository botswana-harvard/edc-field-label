from django import forms

from .models import MyModel, MyOtherModel


class MyModelForm (forms.ModelForm):

    class Meta:
        model = MyModel


class MyOtherModelForm (forms.ModelForm):

    class Meta:
        model = MyOtherModel
