from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Registration(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    BELT_LEVEL_CHOICES = (
        ('13', '13th'),
        ('12', '12th'),
        ('11', '11th'),
        ('10', '10th'),
        ('9', '9th'),
        ('8', '8th'),
        ('7', '7th'),
        ('6', '6th'),
        ('5', '5th'),
        ('4', '4th'),
        ('3', '3rd'),
        ('2', '2nd'),
        ('1', '1st'),
    )
    BELT_TYPE_CHOICES = (
        ('kyu', 'Kyu - colored belts'),
        ('dan', 'Dan - black belts'),
    )
    COUNTRY_CHOICES = (
        ('US', 'United States'),
    )
    US_STATE_CHOICES = (
        ('CO', 'Colorado'),
        ('MO', 'Missouri'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('PA', 'Pennsylvania'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
    )

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    gender = models.CharField(
        _('category'), choices=GENDER_CHOICES, max_length=2,
    )
    birth_date = models.DateField()
    weight = models.IntegerField()
    height = models.CharField(max_length=5)
    is_metric = models.BooleanField(
        help_text=_('Check if your measurements are in metric units.')
    )
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=62)
    state = models.CharField(
        max_length=3, choices=US_STATE_CHOICES, default='UT'
    )
    postal_code = models.CharField(max_length=10)
    country = models.CharField(
        max_length=3, choices=COUNTRY_CHOICES, default='US'
    )
    phone_number = models.IntegerField()
    email = models.EmailField(_('email address'))
    belt_type = models.CharField(max_length=4, choices=BELT_TYPE_CHOICES)
    belt_level = models.CharField(
        choices=BELT_LEVEL_CHOICES, max_length=2,
        help_text=_('Belt number level in kyu or dan.')
    )
    years_training = models.IntegerField(
        help_text=_('Enter 0 if less than 1 year.')
    )

    events = models.CharField(max_length=40)

    instructor_name = models.CharField(max_length=60)
    dojo_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(_('date joined'), default=timezone.now)
    updated_at = models.DateTimeField(_('date updated'), auto_now=True)

    has_payment = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('registration')
        verbose_name_plural = _('registrations')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_registry(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this registered competitor.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
