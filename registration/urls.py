from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='registration_home'),
    url(r'^waiver/$', views.WaiverView.as_view(), name='liability_waiver'),
    url(r'^register/$', views.RegistrationFormView.as_view(), name='registration_form'),
    url(r'^payment/$', views.RegistrationPaymentFormView.as_view(), name='registration_payment_form'),

]
