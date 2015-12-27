from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
# Create your views here.
stripe.api_key =  settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
        pub_key = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == "POST":
		token = request.POST['stripeToken']

		# Create the charge on Stripe's servers - this will charge the user's card
		try:
  			charge = stripe.Charge.create(
      			amount=1000, # amount in cents, again
      			currency="usd",
      			source=token,
      			description="Example charge"
  			)
		except stripe.error.CardError, e:
  			# The card has been declined
  			pass
        context = {}
        template = 'checkout.html'
        return render(request,template,context)
