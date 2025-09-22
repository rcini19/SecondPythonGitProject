from django import forms

class CalcForm(forms.Form):
    a = forms.DecimalField(label="First number", max_digits=20, decimal_places=6)
    b = forms.DecimalField(label="Second number", max_digits=20, decimal_places=6)
    OP_CHOICES = (
        ("+", "Add (+)"),
        ("-", "Subtract (−)"),
        ("*", "Multiply (×)"),
        ("/", "Divide (÷)"),
    )
    op = forms.ChoiceField(label="Operation", choices=OP_CHOICES)