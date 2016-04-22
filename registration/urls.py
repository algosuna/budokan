from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'', views.RegistrationFormView.as_view(), name='registration_form'),
    url(r'payment/', views.RegistrationPaymentFormView.as_view(), name='registration_payment_form'),

]
