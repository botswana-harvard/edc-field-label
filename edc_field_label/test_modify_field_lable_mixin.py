from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from example.admin import MyModelAdmin

from example.models import MyModel


class MockRequest(object):
    pass


class TestReadonlyAdminMixin(TestCase):

    def setUp(self):
        self.request = MockRequest()
        self.my_model = MyModel.objects.create(
            my_first_field="this is just test data 1",
            my_second_field="this is just test data 2"
        )
        self.site = AdminSite()

    def test_replace_field_label(self):
        custom_model_admin = MyModelAdmin(MyModel, self.site)
#         custom_model_admin.replace_labels('my_first_field', )
        print dir(custom_model_admin), 'custom_model_admin'


# from django.db import models
# from django.test import TestCase
# from django.utils import timezone
# 
# from example.forms import MyModelForm
# 
# 
# class TestModel(models.Model):
# 
#     field_1 = models.CharField()
# 
# 
# class TestModifyFieldLableMixin(TestCase):
# 
#     def setUp(self):
#         pass
# 
#     def test_replace_labels_datetime_Value(self):
#         """Test replacing a place holder with a datetime."""
#         form_data = {"my_first_field": "test value 1", "my_second_field": "test value 1"}
#         new_value = timezone.datetime(2016, 12, 12, 3, 23)
#         form = MyModelForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         label = 'This text was last modified on []'
#         new_label = 'This text was last modified on [Monday, December 12, 2016 at 03:23 hours]'
#         self.assertEqual(form.base_fields['my_first_field'].label, label)
#         form.replace_labels('my_first_field', new_value)
#         self.assertEqual(form.base_fields['my_first_field'].label, new_label)
# 
#     def test_replace_labels_non_datetime_Value(self):
#         """Test replacing a place holder with a value."""
#         form_data = {"my_second_field": "test value 1", "my_second_field": "test value 1"}
#         new_value = "last month"
#         form = MyModelForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         new_label = 'The second field text was last modified on [last month] before the first text was modified.'
#         form.replace_labels('my_second_field', new_value)
#         self.assertEqual(form.base_fields['my_second_field'].label, new_label)
# 
#     def test_replace_labels_again(self):
#         """Test replacing a place lable that has been replaced with a value before."""
#         form_data = {"my_second_field": "test value 1", "my_second_field": "test value 1"}
#         new_value = "last month"
#         form = MyModelForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         new_label = 'The second field text was last modified on [last month] before the first text was modified.'
#         form.replace_labels('my_second_field', new_value)
#         self.assertEqual(form.base_fields['my_second_field'].label, new_label)
#         another_new_value = timezone.datetime(2016, 12, 12, 3, 23)
#         form.replace_labels('my_second_field', another_new_value)
#         another_new_label = 'The second field text was last modified on [Monday, December 12, 2016 at 03:23 hours] before the first text was modified.'
#         self.assertEqual(form.base_fields['my_second_field'].label, another_new_label)
