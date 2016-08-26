from django.contrib import admin

from .forms import MyModelForm, MyOtherModelForm
from .models import MyModel, MyOtherModel


class MyModelAdmin(admin.AdminSite):

    form = MyModelForm

    fields = (
        "my_first_field",
        "my_second_field",
    )
    radio_fields = {
        "my_first_field": admin.VERTICAL,
        "my_second_field": admin.VERTICAL}

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(admin.AdminSite):

    form = MyOtherModelForm

    fields = (
        "my_first_field",
        "my_second_field",
    )
    radio_fields = {
        "my_first_field": admin.VERTICAL,
        "my_second_field": admin.VERTICAL}

admin.site.register(MyOtherModel, MyOtherModelAdmin)
