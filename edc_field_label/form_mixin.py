import re

from datetime import datetime


class ModifyFormLabelMixin:
    """Replace a from label datetime placeholder with a datetime value."""

    def get_form_post(self, form, request, obj, **kwargs):
        return self.replace_labels(form, request)

    def replace_labels(self, field_name, replacement_value):
        WIDGET = 1
        for _, fld in enumerate(self.base_fields.items()):
            if type(replacement_value) is datetime:
                new_value = replacement_value.strftime('%A, %B %d, %Y at %H:%M hours')
            elif type(replacement_value) is not str:
                new_value = str(replacement_value)
            else:
                new_value = replacement_value
            if field_name == fld[0]:
                if not re.match(r'^\d+\.', str(fld[WIDGET].label)) and re.search(r"\[\]", str(fld[WIDGET].label)):
                    fld[WIDGET].label = re.sub("\[\]", new_value, fld[WIDGET].label)
