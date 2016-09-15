from django.contrib import admin

from edc_field_label.admin_mixin import ModifyFormLabelMixin
from .models import MyModel, MyOtherModel

from .forms import MyModelForm, MyOtherModelForm


class MyModelAdmin(ModifyFormLabelMixin, admin.ModelAdmin):

    form = MyModelForm

    fields = ['my_other_model', 'my_first_field', 'my_second_field']
    list_display = ('my_first_field', 'my_second_field')

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(admin.ModelAdmin):

    form = MyOtherModelForm

    fields = ['my_first_field', 'report_datetime']

admin.site.register(MyOtherModel, MyOtherModelAdmin)
