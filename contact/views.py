from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'address': address,
                'email': email,
                'phonenumber': phonenumber
            })

            send_mail('Hello from Atheesh', 'Hello there. This is an automated message', 'atks@falconorange.com', ['bhrj@falconorange.com'], html_message=html)

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form
    })