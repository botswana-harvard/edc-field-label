from django.contrib import admin

from .forms import MyModelForm, MyOtherModelForm
from .models import MyModel, MyOtherModel


class MyModelAdmin(admin.AdminSite):

    form = MyModelForm

    fields = (
        "my_first_field",
        "my_second_field",
    )

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(admin.AdminSite):

    form = MyOtherModelForm

    fields = (
        "my_first_field",
        "my_second_field",
    )

admin.site.register(MyOtherModel, MyOtherModelAdmin)
