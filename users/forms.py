from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'name', 'gender', 'age', 'image', 'date_of_birth', 'college_name', 'city', 'password1',
                  'password2']
        help_texts = {
            # 'image': _('Your profile picutre can be accessed by all the Campers'),
            # 'email': _('Use the email which is submitted to World Konkani Centre'),
        }
        labels = {
            # 'batch': _('VKSSF Batch'),
            'image': _('Profile picture'),
            'name': _('Full name'),
            'college_name': _('College name / School name / Company name')
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'name', 'gender', 'age', 'image', 'date_of_birth', 'college_name', 'city']

        help_texts = {
            'date_of_birth': _('Please enter in this format <strong>yyyy-mm-dd</strong>'),
            # 'email': _('Use the email which is submitted to World Konkani Centre'),

        }
        labels = {
            # 'batch': _('VKSSF Batch'),
            'image': _('Profile picture'),
            'name': _('Full name')
        }


