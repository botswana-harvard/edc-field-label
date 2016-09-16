from datetime import datetime

from django.db import models


class MyOtherModel (models.Model):

    my_first_field = models.CharField(
        verbose_name='This is just a test field.',
        default=None,
        null=True,
        blank=True,
        max_length=50,
        help_text=""
    )

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        default=datetime.now,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    class Meta:
        app_label = 'example'
        verbose_name = "My Other Model"
        verbose_name_plural = "My Other Model"


class MyModel (models.Model):

    my_other_model = models.ForeignKey(MyOtherModel, null=True)

    my_first_field = models.CharField(
        verbose_name="We last spoke with you on last_visit_date and scheduled an appointment for you "
                     "in an HIV care clinic on last_appt_date. Did you keep that appointment?",
        default=None,
        null=True,
        blank=True,
        max_length=50,
        help_text=""
    )

    my_second_field = models.CharField(
        verbose_name='The second field text was last modified on [] before the first text was modified.',
        default=None,
        null=True,
        blank=True,
        max_length=50,
        help_text=""
    )

    def previous_visit(self):
        return self.my_other_model

    def previous_appt(self):
        return self.my_other_model

    class Meta:
        app_label = 'example'
        verbose_name = "My Model"
        verbose_name_plural = "My Model"
