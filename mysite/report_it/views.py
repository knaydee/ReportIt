from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import IncidentLog

def index(request):
    return render(request, 'report_it/index.html')

def log(request):
    if request.method == 'GET':
        form = IncidentLog(label_suffix='')
    else:
        form = IncidentLog(request.POST)
        if form.is_valid():
            email = form.cleaned_data['your_email']
            message = "Name(s): " + form.cleaned_data['name'] + "\n" + "Location: " + form.cleaned_data['location'] + "\n" + "Context/Situation: " + form.cleaned_data['context'] + "\n" + "Quote: " + form.cleaned_data['quote'] + "\n" + "Tags: " + form.cleaned_data['tags']
            try:
                send_mail('Incident Report', message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found. Please try again.')
            return HttpResponseRedirect('confirmation')
    return render(request, 'report_it/log.html', {'form': form})

def confirmation(request):
    return render(request, 'report_it/confirmation.html')


