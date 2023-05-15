from django import forms

from users.models import Weight


class WeightFormulaForm(forms.Form):
    weight_formula = forms.ModelChoiceField(
        queryset=Weight.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect
    )