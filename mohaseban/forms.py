from django import forms
class NameForm(forms.Form):
     your_name = forms.CharField(initial='Your name', max_length=100)
     sender = forms.EmailField(initial='email')
     #sender.widget.attrs.update({'class':"contatct-form"})
     message = forms.CharField(widget=forms.Textarea)
     #cc_myself = forms.BooleanField(required=False)

class Employee(forms.Form):
	first_name = forms.CharField(initial='first_name name', max_length=100)
	last_name = forms.CharField(initial='last name', max_length=100)
	email = forms.EmailField(initial='email')
	resume = forms.CharField(widget=forms.Textarea)
