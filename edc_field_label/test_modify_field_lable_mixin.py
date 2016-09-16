from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from example.admin import MyModelAdmin

from example.models import MyModel, MyOtherModel
from django.utils import timezone


class MockRequest(object):
    pass


class TestReadonlyAdminMixin(TestCase):

    def setUp(self):
        self.request = MockRequest()
        self.site = AdminSite()

    def test_replace_labels_not_replaced(self):
        """Test replacing a place holder with a datetime."""
        custom_model_admin = MyModelAdmin(MyModel, self.site)
        form = custom_model_admin.get_form(self.request)
        label = 'We last spoke with you on last_visit_date and scheduled an appointment for you in an HIV care clinic on last_appt_date. Did you keep that appointment?'
        self.assertEqual(form.base_fields['my_first_field'].label, label)

    def test_replace_labels_replaced(self):
        """Test replacing a place holder with a datetime."""
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
