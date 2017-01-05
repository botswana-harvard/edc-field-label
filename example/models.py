from django.db import models


class MyLocationModel (models.Model):

    community = models.CharField(
        verbose_name='Community name',
        default=None,
        null=True,
        blank=True,
        max_length=50,
        help_text=""
    )

    class Meta:
        app_label = 'example'
        verbose_name = "My Location Model"
        verbose_name_plural = "My Location Model"


class MyModel (models.Model):

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
        verbose_name='Since we last saw you at last_seen_location, did you play soccer?',
        default=None,
        null=True,
        blank=True,
        max_length=50,
        help_text=""
    )

    class Meta:
        app_label = 'example'
        verbose_name = "My Model"
        verbose_name_plural = "My Model"
