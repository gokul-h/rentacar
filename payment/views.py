from django.shortcuts import render
from main.models import car
import razorpay
from .models import carorder
from django.views.decorators.csrf import csrf_exempt


def checkout(request):
    if request.method == "POST":
        # To show on page
        car_id = request.POST['id']
        car1 = car.objects.get(id=car_id)
        weeks = 1

        gst = int(car1.price * weeks * 0.18)
        total = int(car1.price * weeks) + gst
        total_new = total * 100
        username = request.user.username
        usermail = request.user.email

        # For payment
        # Add payment keys from RazorPay Here
        client = razorpay.Client(auth=("", ""))
        DATA = {
            "amount": total_new,
            "currency": "INR",
            "payment_capture": '1',
        }
        payment = client.order.create(data=DATA)
        carorder1 = carorder(username=username, vehicle_id=car_id, price=total_new, payment_id=payment['id'])
        carorder1.save()
        return render(request, 'checkout.html',
                      {'username': username, 'carval': car1, 'gst': gst, 'total': total, 'payment': payment,
                       'usermail': usermail})
    else:
        return render(request, 'checkout.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = carorder.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
    return render(request, 'success.html')
