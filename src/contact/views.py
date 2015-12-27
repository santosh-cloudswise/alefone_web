from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

from .forms import ContactForm
def home(request):
	title = "Contact"
	form = ContactForm(request.POST or None)
	confirm_message = None
	if form.is_valid():
		comment=form.cleaned_data['comment']
		name=form.cleaned_data['name']
		subject = 'Message from CloudsWise.com'
		msg = '%s %s' %(comment ,name)
		to_us = [ settings.EMAIL_HOST_USER]
		frm = form.cleaned_data['email']
		send_mail(subject,msg,frm,to_us, fail_silently=False)
#		print request.POST
		title = "Thank You"
		confirm_message =  """
		Thank you for your message. We have received it and are reviewing it
		"""
		form = None
		context = {
		'title': title,
		'confirm_message': confirm_message
		}

        context = locals()
        template = 'contact.html'
        return render(request, template, context)
