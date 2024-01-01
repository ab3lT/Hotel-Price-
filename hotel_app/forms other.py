from django import forms

class DateInputForm(forms.Form):
    check_in = forms.DateField(widget=forms.SelectDateWidget())
    check_out = forms.DateField(widget=forms.SelectDateWidget())
    booking_advance = forms.IntegerField(min_value=0, required=False, help_text="Days in advance of booking")
    num_persons = forms.IntegerField(min_value=1,  help_text="Number of persons")
    flexible_cancellation = forms.BooleanField(required=False, help_text="Flexible cancellation option")