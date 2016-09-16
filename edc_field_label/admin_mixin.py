import re

from datetime import datetime


class ModifyFormLabelMixin(object):
    """Replace a from label datetime placeholder with a datetime value."""
    replacements = {
        'first_rep': {
            'field_attr': 'my_first_field',
            'placeholder': 'last_visit_date',
            'replacement_attr': 'report_datetime',
            'attr': 'previous_visit',
        },
        'second_rep': {
            'field_attr': 'my_first_field',
            'placeholder': 'last_appt_date',
            'replacement_attr': 'report_datetime',
            'attr': 'previous_appt',
        },
    }

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModifyFormLabelMixin, self).get_form(request, obj, **kwargs)
        return self.replace_labels(form, obj)

    def convert_to_string(self, value):
        """Convert a value to string, if its a date make it a string date version"""
        if type(value) is datetime:
            new_value = value.strftime('%A, %B %d, %Y at %H:%M hours')
        elif type(value) is not str:
            new_value = str(value)
        else:
            new_value = value
        return new_value

    def replace_labels(self, form, obj):
        WIDGET = 1
        replacement_value = None
        for _, fld in enumerate(form.base_fields.items()):
            for _, values in self.replacements.iteritems():
                if values['field_attr'] == fld[0] and obj:
                    replacement_value_obj = getattr(obj, values['attr'])()
                    replacement_value = self.convert_to_string(getattr(replacement_value_obj, values['replacement_attr']))
                    if re.search(r'{}'.format(values['placeholder']), str(fld[WIDGET].label)):
                        fld[WIDGET].label = re.sub('{}'.format(values['placeholder']), replacement_value, fld[WIDGET].label)
        return form
