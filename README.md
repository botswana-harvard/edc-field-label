# edc-field-label
Modify or replace a form field label

###Installation


pip install git+https://github.com/botswana-harvard/edc-field-label@develop#egg=edc_field_label

add to settings.py:


INSTALLED_APPS = [
....
'edc_field_lable.apps.AppConfig',
...]

###Usage


A field label on the form is a string that is specified as a verbose name on the models. The field label is usually
the question on the form field or or a description of what should be field on the form field.

This app provides a way to modify the field label on opening the form, but substituting a place holder with a value
provided for a specified field.

First use the admin mixin that bring in the method that modifies a label. The replacement value can be a datetime or any other type.

Defination of the custom model admin. Define the 'replacements' config dictionary in you model admin.

	class MyModelAdmin (ModifyFormLabelMixin, admin.ModelAdmin):

		replacements = {
            'first_rep': {
                'field_attr': 'my_first_field',
                'place_holder': 'last_visit_date',
                'place_holder_value': value,
            },
            'second_rep': {
                'field_attr': 'my_first_field',
                'place_holder': 'last_appt_date',
                'place_holder_value': value,
            },
        }
		
        form = MyModelForm

    	fields = ['my_other_model', 'my_first_field', 'my_second_field']

	admin.site.register(MyModel, MyModelAdmin)

The models look like this

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
 
 