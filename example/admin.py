from django.contrib import admin

from edc_field_label.admin_mixin import ModifyFormLabelMixin
from .models import MyModel, MyOtherModel, MyLocationModel

from .forms import MyModelForm, MyOtherModelForm, MyLocationModelForm


class MyModelAdmin(ModifyFormLabelMixin, admin.ModelAdmin):

    form = MyModelForm

    fields = ['my_other_model', 'my_first_field', 'my_second_field']

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(admin.ModelAdmin):

    form = MyOtherModelForm

    fields = ['my_first_field', 'report_datetime']

admin.site.register(MyOtherModel, MyOtherModelAdmin)


class MyLocationModelAdmin(admin.ModelAdmin):

    form = MyLocationModelForm

    fields = ['community']

admin.site.register(MyLocationModel, MyLocationModelAdmin)
