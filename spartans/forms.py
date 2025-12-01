from django import forms
from usermanagement.models.user_model import User

class Forget_pwForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No User Registered With Email")
