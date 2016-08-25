from django.test import TestCase
from django.db import models


class TestModel(models.Model):

    field_1 = models.CharField()


class TestModifyFieldLableMixin(TestCase):

    def setUp(self):
        pass

    def test_replace_labels(self):
        pass
#         form = None
#         request = None
#         ModifyFormLabelMixin.replace_labels(form, request)
