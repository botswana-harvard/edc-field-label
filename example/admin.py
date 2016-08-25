from django.contrib import admin

from edc_field_label.admin_mixin import ModifyFormLabelMixin

from .forms import MyModelForm, MyOtherModelForm
from .models import MyModel, MyOtherModel


class MyModelAdmin(ModifyFormLabelMixin, admin.AdminSite):

    form = MyModelForm
    # QUERY_MODEL_PARAMETERS = {"field_name_to_modify_lable": [query_model, "replacement_model_field_attribute", "foreinkey_model", "foreign_key_field_attribute", "query_model_field_attribute"]}
#     QUERY_MODEL_PARAMETERS = {"my_first_field": [SubjectConsent, "consent_datetime", SubjectVisit, "subject_visit", "subject_identifier"],
#                               "my_second_field": [SubjectConsent, "consent_datetime", SubjectVisit, "subject_visit", "subject_identifier"]}

    fields = (
        "my_first_field",
        "my_second_field",
    )
    radio_fields = {
        "my_first_field": admin.VERTICAL,
        "my_second_field": admin.VERTICAL}

admin.site.register(MyModel, MyModelAdmin)


class MyOtherModelAdmin(ModifyFormLabelMixin, admin.AdminSite):

    form = MyOtherModelForm

    fields = (
        "my_first_field",
        "my_second_field",
    )
    radio_fields = {
        "my_first_field": admin.VERTICAL,
        "my_second_field": admin.VERTICAL}

admin.site.register(MyOtherModel, MyOtherModelAdmin)
