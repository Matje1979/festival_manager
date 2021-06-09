from django import 	forms
from.models import Visitor


class EventVisitorForm(forms.ModelForm):
	class Meta:
		model = Visitor
		fields = ['first_name', 'last_name', 'email']