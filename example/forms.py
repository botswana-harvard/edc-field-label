from django import forms

from edc_field_label.form_mixin import ModifyFormLabelMixin

from .models import MyModel, MyOtherModel


class MyModelForm (ModifyFormLabelMixin, forms.ModelForm):

    class Meta:
        model = MyModel
        fields = '__all__'


class MyOtherModelForm (forms.ModelForm):

    class Meta:
        model = MyOtherModel
        fields = '__all__'
