from django import forms
from material import Layout, Fieldset, Row, Column, Span2, Span3, Span4

from .models import Registration


class RegistrationForm(forms.ModelForm):

    EVENT_CHOICES = (
        ('kata', 'Kata'),
        ('kumite', 'Kumite'),
        ('tkata', 'Team kata'),
        ('tkumite', 'Team kumite'),
    )

    class Meta:
        model = Registration
        exclude = (
            'country',
            'created_at',
            'updated_at',
            'has_payment',
        )

    events = forms.MultipleChoiceField(
        choices=EVENT_CHOICES, widget=forms.CheckboxSelectMultiple
    )
    accept_terms = forms.BooleanField(required=True)

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
            Row(Span3('gender'), Span2('height'), Span2('weight'), Span4('is_metric')),
            Row('belt_type', 'belt_level', 'years_training'),
            Row(Span3('events'), Column('instructor_name', 'dojo_name', span_columns=9)),
        ),
        'accept_terms',
    )
