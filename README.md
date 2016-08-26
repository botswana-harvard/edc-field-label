# edc-field-label
Modify or replace a form field label

###Installation




###Usage


A field label on the form is a string that is specified as a verbose name on the models. The field label is usually
the question on the form field or or a description of what should be field on the form field.

This app provides a way to modify the field label on opening the form, but substituting a place holder with a value
provided for a specified field.

First use the form mixin that bring in the method that modifies a label and pass the two parameters to the method,
'field_name' and 'replacement value' for the place holder. The replacement value can be a datetime or any other type.

	class MyModelForm (ModifyFormLabelMixin, forms.ModelForm):

    class Meta:
        model = MyModel
    
 Call the methods in a place like 'get_form' or have a method that you can override and call that method in 'get_form'.
 
 	form.replace_labels('field_name', value)
 
 When a form is loaded a place holder will be replaced by the 'value' passed on the method.