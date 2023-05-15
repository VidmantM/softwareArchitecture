from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Profile, Skill, Interest, Project
from .models import Weight


class SignUpForm(UserCreationForm):
    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        if User.objects.filter(username=username).exists():
            raise ValidationError("User exists")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileEditForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(queryset=Interest.objects.all(), widget=forms.CheckboxSelectMultiple)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Profile
        fields = ['skills', 'interests', 'projects']


class WeightFormulaForm(forms.Form):
    weight_formula = forms.ModelChoiceField(
        queryset=Weight.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect
    )