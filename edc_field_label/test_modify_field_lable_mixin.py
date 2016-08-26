from django.db import models
from django.test import TestCase
from django.utils import timezone

from example.forms import MyModelForm


class TestModel(models.Model):

    field_1 = models.CharField()


class TestModifyFieldLableMixin(TestCase):

    def setUp(self):
        pass

    def test_replace_labels_datetime_Value(self):
        form_data = {"my_first_field": "test value 1", "my_second_field": "test value 1"}
        new_value = timezone.datetime(2016, 12, 12, 3, 23)
        form = MyModelForm(data=form_data)
        self.assertTrue(form.is_valid())
        label = 'This text was last modified on []'
        new_label = 'This text was last modified on Monday, December 12, 2016 at 03:23 hours'
        self.assertEqual(form.base_fields['my_first_field'].label, label)
        form.replace_labels('my_first_field', new_value)
        self.assertEqual(form.base_fields['my_first_field'].label, new_label)

    def test_replace_labels_non_datetime_Value(self):
        form_data = {"my_second_field": "test value 1", "my_second_field": "test value 1"}
        new_value = "last month"
        form = MyModelForm(data=form_data)
        self.assertTrue(form.is_valid())
        label = 'The second field text was last modified on [] before the first text was modified.'
        new_label = 'The second field text was last modified on last month before the first text was modified.'
        self.assertEqual(form.base_fields['my_second_field'].label, label)
        form.replace_labels('my_second_field', new_value)
        self.assertEqual(form.base_fields['my_second_field'].label, new_label)
