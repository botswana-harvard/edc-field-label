from django.contrib import admin

from edc_field_label.admin_mixin import ModifyFormLabelMixin
from .models import MyModel, MyLocationModel

from .forms import MyModelForm, MyLocationModelForm


class MyModelAdmin(ModifyFormLabelMixin, admin.ModelAdmin):

    form = MyModelForm

    fields = ['my_first_field', 'my_second_field']

admin.site.register(MyModel, MyModelAdmin)


class MyLocationModelAdmin(admin.ModelAdmin):

    form = MyLocationModelForm

    fields = ['community']

admin.site.register(MyLocationModel, MyLocationModelAdmin)
