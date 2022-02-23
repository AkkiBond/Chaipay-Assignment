from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe

stripe.api_key = 'sk_test_51KUrWsSAxXENFj4Fnf7a1M5UtSFmFWRTnNeAxnj0USqC2mMxRE9mZ59KQ4UFwQQSzECoNDrQfHoPriy7beJ2Vh1300vfyUMhEu'

@api_view(['POST'])
def create_charge(request):
    payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 2,
                "exp_year": 2023,
                "cvc": "314",
            },
            )
    response = stripe.PaymentIntent.create(
            amount=1099,
            currency='inr',
            payment_method = payment_method,
            payment_method_types=["card"],
            confirm='true',
            confirmation_method='automatic',
            capture_method='manual'
            )
    return Response(response)


@api_view(['POST'])
def capture_charge(request):
    id = request.data.get('id')
    res = stripe.PaymentIntent.capture(
        id,
        )
    return Response(res)


@api_view(['POST'])
def create_refund(request):
    pid = request.data.get('pid')
    refundObj = stripe.Refund.create(
        payment_intent=pid,
        )
    return Response(refundObj)


@api_view(['GET'])
def list_charges(request):
    paymentIntents = stripe.PaymentIntent.list(limit=3)
    return Response(paymentIntents)