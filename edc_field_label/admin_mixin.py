import re

from datetime import datetime

from django.utils import timezone


class ModifyFormLabelMixin:
    """Replace a from label datetime placeholder with a datetime value."""

    def get_form(self, form, request, obj, **kwargs):
        form = super(ModifyFormLabelMixin, self).get_form(form, request, obj, **kwargs)
        return self.replace_labels(form, request)

    def convert_to_string(self, value):
        """Convert a value to string, if its a date make it a string date version"""
        if type(value) is datetime:
            new_value = value.strftime('%A, %B %d, %Y at %H:%M hours')
        elif type(value) is not str:
            new_value = str(value)
        else:
            new_value = value
        return new_value

    def replace_labels(self, form, request):
        # TODO: get the value from the request object.
        value = timezone.now()  # This value should come from the request object.
        WIDGET = 1
        for _, fld in enumerate(form.base_fields.items()):
            replacement_value = self.convert_to_string(value)
            if not re.match(r'^\d+\.', str(fld[WIDGET].label)) and re.search(r'\[.*\]', str(fld[WIDGET].label)):
                fld[WIDGET].label = re.sub('\[.*\]', '[' + replacement_value + ']', fld[WIDGET].label)
        return form
