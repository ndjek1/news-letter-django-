from django.shortcuts import render, redirect
from django.contrib import messages

from main.models import Subscriber
from .forms import NewsletterForm, SubscriptionForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'index.html')
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Save the email to the database
            try:
                Subscriber.objects.create(email=email)
                messages.success(request, f"Successfully Subscribed {email}")
                return redirect('subscribe')
            except Exception as e:
                 messages.error(request, "You already subscribed!")
                 return render(request, 'index.html', {'error_message': "You already subscribed!"})
        else:
            messages.error(request, "Invalid email address provided")
            return render(request, 'index.html', {'error_message': "Invalid email address provided"})
    else:
        form = SubscriptionForm()
    return render(request, 'index.html', {'form': form})

def dashboard(request):
    subscribers = Subscriber.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = [subscriber.email for subscriber in subscribers]
            send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    recipient_list,
                    fail_silently=False,
                )
            messages.success(request, "Successfully sent emails to all subscribers")
            return redirect('dashboard')
        else:
             messages.error(request, "Invalid email data")
             return render(request, 'dashboard.html',{'subscribers':subscribers,'form':form,})
    else:
        form = NewsletterForm()
    return render(request, 'dashboard.html',{'subscribers':subscribers,'form':form,})