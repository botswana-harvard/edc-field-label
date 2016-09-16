from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from example.admin import MyModelAdmin

from example.models import MyModel, MyOtherModel, MyLocationModel
from django.utils import timezone


class MockRequest(object):
    pass


class TestReadonlyAdminMixin(TestCase):

    def setUp(self):
        self.request = MockRequest()
        self.replacements = {
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
            'third_rep': {
                'field_attr': 'my_second_field',
                'placeholder': 'last_seen_location',
                'replacement_attr': 'community',
                'attr': 'previous_location',
            },
        }
        self.site = AdminSite()

    def test_replace_labels_not_replaced(self):
        """Test if the original field label return with place holder"""
        custom_model_admin = MyModelAdmin(MyModel, self.site)
        form = custom_model_admin.get_form(self.request)
        label = 'We last spoke with you on last_visit_date and scheduled an appointment for you in an HIV care clinic on last_appt_date. Did you keep that appointment?'
        self.assertEqual(form.base_fields['my_first_field'].label, label)

    def test_replace_labels(self):
        """Test replacing a place holder with a value on a label."""
        custom_model_admin = MyModelAdmin(MyModel, self.site)
        form = custom_model_admin.get_form(self.request)
        label = 'We last spoke with you on last_visit_date and scheduled an appointment for you in an HIV care clinic on last_appt_date. Did you keep that appointment?'
        self.assertEqual(form.base_fields['my_first_field'].label, label)

        my_other_model = MyOtherModel.objects.create(
            my_first_field="this is just test data 1",
            report_datetime=timezone.now())
        my_model = MyModel.objects.create(
            my_other_model=my_other_model,
            my_first_field="this is just test data 1",
            my_second_field="this is just test data 2"
        )
        new_value = timezone.datetime(2016, 12, 12, 3, 23)
        my_other_model.report_datetime = new_value
        my_other_model.save()

        new_label = 'We last spoke with you on Monday, December 12, 2016 at 03:23 hours and scheduled an appointment for you in an HIV care clinic on Monday, December 12, 2016 at 03:23 hours. Did you keep that appointment?'
        form = custom_model_admin.get_form(self.request, my_model)
        self.assertEqual(form.base_fields['my_first_field'].label, new_label)

    def test_replace_more_labels(self):
        """Test replacing a place holder on more than one field."""
        custom_model_admin = MyModelAdmin(MyModel, self.site)
        custom_model_admin.replacements = self.replacements
        form = custom_model_admin.get_form(self.request)
        my_first_field_label = 'We last spoke with you on last_visit_date and scheduled an appointment for you in an HIV care clinic on last_appt_date. Did you keep that appointment?'
        self.assertEqual(form.base_fields['my_first_field'].label, my_first_field_label)
        my_second_field_label = 'Since we last saw you at last_seen_location, did you play soccer?'
        self.assertEqual(form.base_fields['my_second_field'].label, my_second_field_label)

        my_location_model = MyLocationModel.objects.create(community='test_community')
        my_other_model = MyOtherModel.objects.create(
            my_location_model=my_location_model,
            my_first_field="this is just test data 1",
            report_datetime=timezone.now())
        my_model = MyModel.objects.create(
            my_other_model=my_other_model,
            my_first_field="this is just test data 1",
            my_second_field="this is just test data 2"
        )
        my_first_field_new_value = timezone.datetime(2016, 12, 12, 3, 23)
        my_other_model.report_datetime = my_first_field_new_value
        my_other_model.save()

        my_first_field_new_label = 'We last spoke with you on Monday, December 12, 2016 at 03:23 hours and scheduled an appointment for you in an HIV care clinic on Monday, December 12, 2016 at 03:23 hours. Did you keep that appointment?'
        form = custom_model_admin.get_form(self.request, my_model)
        self.assertEqual(form.base_fields['my_first_field'].label, my_first_field_new_label)

        my_second_field_new_label = 'Since we last saw you at test_community, did you play soccer?'
        self.assertEqual(form.base_fields['my_second_field'].label, my_second_field_new_label)
