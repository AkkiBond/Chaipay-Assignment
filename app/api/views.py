from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe
import urllib.request


stripe.api_key = 'sk_test_51KUrWsSAxXENFj4Fnf7a1M5UtSFmFWRTnNeAxnj0USqC2mMxRE9mZ59KQ4UFwQQSzECoNDrQfHoPriy7beJ2Vh1300vfyUMhEu'

@api_view(['POST'])
def create_charge(request):
    """
        View for creating charge. First we are creating
        a payment method for testing then passing that
        to create a payment intent.

        urllib is being used for performing the action
        for confirming the payment.
    """

    payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 2,
                "exp_year": 2023,
                "cvc": "314",
            },
            )

    createdObj = stripe.PaymentIntent.create(
            amount=1099,
            currency='inr',
            payment_method = payment_method,
            payment_method_types=["card"],
            confirm='true',
            confirmation_method='automatic',
            capture_method='manual'
            )

    webUrl = urllib.request.urlopen(createdObj.next_action.use_stripe_sdk.stripe_js)

    return Response(createdObj)


@api_view(['POST'])
def capture_charge(request,pid):
    """
        View for capturing the paymentIntent. It requires
        a paymentIntent as input for capturing the paymentIntent.
    """

    try:
        capturedObj = stripe.PaymentIntent.capture(
            pid,
            )
    except Exception as e:
        raise e
    return Response(capturedObj)


@api_view(['POST'])
def create_refund(request,pid):
    """
        View for creating a refund for a particular
        paymentIntent which requires paymentIntent id.
    """

    try:
        refundObj = stripe.Refund.create(
            payment_intent=pid,
            )
    except Exception as e:
        return e
    return Response(refundObj)


@api_view(['GET'])
def list_charges(request):
    """
        View for listing all the paymentIntents.
    """

    paymentIntents = stripe.PaymentIntent.list()
    return Response(paymentIntents)