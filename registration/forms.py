from django import forms
from material import Layout, Fieldset, Row, Column, Span2, Span3

from .models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        exclude = (
            'country',
            'created_at',
            'updated_at',
            'has_payment',
        )

    events = forms.MultipleChoiceField(
        choices=Registration.EVENT_CHOICES, widget=forms.CheckboxSelectMultiple
    )
    accept_terms = forms.BooleanField(required=True, label='I agree')

    layout = Layout(
        Fieldset(
            'Basic Info',
            Row('first_name', 'last_name'),
            Row('address1', 'address2'),
            Row(Span3('city'), 'state', Span2('postal_code')),
            Row('phone_number', 'email', 'birth_date'),
        ),
        Fieldset(
            'Competition Info',
            Row('gender', 'weight', 'is_metric'),
            Row('belt_type', 'belt_level', 'years_training'),
            Row('years_training', 'competition_level'),
            Row(Span3('events'), Column(
                'instructor_name', 'dojo_name', 'karate_style', span_columns=9
            )),
        ),
        'accept_terms',
    )
