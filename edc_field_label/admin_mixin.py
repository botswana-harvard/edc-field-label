import re

from datetime import datetime


class ModifyFormLabelMixin(object):
    """Replace a from label datetime placeholder with a datetime value."""
    replacements = {}

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModifyFormLabelMixin, self).get_form(request, obj, **kwargs)
        return self.replace_labels(form)

    def convert_to_string(self, value):
        """Convert a value to string, if its a date make it a string date version"""
        if type(value) is datetime:
            new_value = value.strftime('%A, %B %d, %Y at %H:%M hours')
        elif type(value) is not str:
            new_value = str(value)
        else:
            new_value = value
        return new_value

    def replace_labels(self, form):
        """Replace a place holder on a label with a value."""
        WIDGET = 1
        place_holder_value = None
        for _, fld in enumerate(form.base_fields.items()):
            for _, values in self.replacements.items():
                if values['field_attr'] == fld[0]:
                    place_holder_value = values['place_holder_value']
                    if place_holder_value:
                        # Convert the value for the place holder to string
                        place_holder_value = self.convert_to_string(values['place_holder_value'])
                        if re.search(r'{}'.format(values['place_holder']), str(fld[WIDGET].label)):
                            fld[WIDGET].label = re.sub(
                                '{}'.format(values['place_holder']),
                                place_holder_value, fld[WIDGET].label)
        return form
