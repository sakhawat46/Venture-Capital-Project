from django import forms
from venture_app.models import Member


class MemberForm(forms.ModelForm):
    # arrivals = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}), label="")
    # leaving = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}), label="")
    # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Name'}), label="")
    # mobile_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}), label="")
    # # tour_place = forms.CharField(widget = forms.TextInput(attrs={}),label="")
    # # tour_place = forms.ModelChoiceField(queryset=Book.objects.all())
    starting_date = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}))

    class Meta:
        model = Member
        # fields = ['tour_place', 'name', 'mobile_number', 'arrivals', 'leaving']
        fields = '__all__'