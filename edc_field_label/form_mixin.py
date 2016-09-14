import re

from datetime import datetime


class ModifyFormLabelMixin:
    """Replace a from label datetime placeholder with a datetime value."""

    def get_form_post(self, form, request, obj, **kwargs):
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

    def replace_labels(self, field_name, replacement_value1):
        WIDGET = 1
        for _, fld in enumerate(self.base_fields.items()):
            replacement_value1 = self.convert_to_string(replacement_value1)
            if field_name == fld[0]:
                if not re.match(r'^\d+\.', str(fld[WIDGET].label)) and re.search(r'\[.*\]', str(fld[WIDGET].label)):
                    fld[WIDGET].label = re.sub('\[.*\]', '[' + replacement_value1 + ']', fld[WIDGET].label)
