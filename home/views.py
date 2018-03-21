from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse

from .contact_form import ContactForm

def index(request):
    return render(request, 'home/index.html')

def contact_me(request):
    form = ContactForm(request.POST)
    context = {
        "form": form
    }
    return render(request, 'home/contact_me.html', context)

def thank_you(request):


    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get("First_name") + " " + form.cleaned_data.get("Last_name")
        if form.cleaned_data.get("Phone"):
            phone = form.cleaned_data.get("Phone")
        else:
            phone = "N/A"
        email = form.cleaned_data.get("Email")
        subject = form.cleaned_data.get("Subject")
        message = form.cleaned_data.get("Message")
        from_email = settings.EMAIL_HOST_USER
        to_email = from_email
        contact_message = "%s: \n %s \n via %s" %(name, message, email)

        mail = EmailMessage(subject, contact_message, from_email, [to_email])
        mail.send(fail_silently=False)
        return render(request, 'home/thank_you.html')

    return HttpResponse(request, 'home/contact_me.html', {"message": "<p>Please ensure all information is valid.</p>"})


def portfolio(request):
    return render(request, 'home/portfolio.html')