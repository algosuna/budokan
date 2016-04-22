from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from paypal.standard.forms import PayPalPaymentsForm

from .forms import RegistrationForm


class RegistrationFormView(FormView):
    template_name = 'registration/form.html'
    form_class = RegistrationForm


class RegistrationPaymentFormView(FormView):
    template_name = 'registration/payment_form.html'
    form_class = PayPalPaymentsForm

    def get_form_kwargs(self):
        kwargs = super(RegistrationPaymentFormView, self).get_form_kwargs()
        kwargs.update({
            'business': 'receiver_email@example.com',
            'amount': '10000',
            'item_name': 'IMA Championship Registration',
            'invoice': 'unique-invoice-id',
            'notify_url': 'https://example.com' + reverse('paypal-ipn'),
            'return_url': 'https://example.com/your-return-location',  # success page?
            'cancel_return': 'https://example.com/your-cancel-location',  # cancel pmt page
        })
        return kwargs


class DisclaimerTemplateView(TemplateView):
    template_name = 'registration/disclaimer.html'
