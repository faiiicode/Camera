from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review, Callback,mailstore
from .forms import Callform


# Create your views here.
def view(request):
    product = Product.objects.all()
    review = Review.objects.all()
    return render(request, "index.html", {'product': product, 'review': review})


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        message = request.POST['message']

        callbk = Callback(name=name,email=email,Phone=Phone,message=message)
        callbk.save()
        return redirect('/')
    return render(request,"registration.html")

def subscribe(request):
    if request.method == 'POST':
         email= request.POST['email']
         callbak =mailstore(email=email)
         callbak.save()
         return redirect('/')
    return render(request,"newsletter.html")

