import imp
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html');

def sendmail(request):
    if request.method == 'POST':
        name = request.POST['firstname']
        email = request.POST['email']
        message = request.POST['message']

        send_mail('Contact form',
        message + ' from ' + name + ' email ' + email,
        settings.EMAIL_HOST_USER,
        ['kunalyadav2003@gmail.com'],
        fail_silently=False)
    return render(request, 'index.html')