from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Subscription, Order, ContactMessage, Service, Gallery
from .forms import OrderForm

# Create your views here.

def index(request):
    subscriptions = Subscription.objects.all()
    services = Service.objects.filter(is_active=True).order_by('order')
    gallery_items = Gallery.objects.filter(is_active=True).order_by('order')
    return render(request, 'index.html', {
        'subscriptions': subscriptions,
        'services': services,
        'gallery_items': gallery_items,
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        return HttpResponse('Сообщение отправлено')
    return render(request, 'contact.html')

def order_subscription(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.subscription = subscription
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    
    return render(request, 'order.html', {
        'form': form,
        'subscription': subscription
    })

def order_success(request):
    return render(request, 'order_success.html')
