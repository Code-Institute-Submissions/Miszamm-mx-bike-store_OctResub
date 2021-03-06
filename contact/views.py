from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .models import Contact


def contact(request):

    if request.POST:
        to_email = settings.DEFAULT_ORDER_EMAIL
        contact_email = request.POST['email']
        phone = request.POST['phone']
        company = request.POST['company']
        message = request.POST['message']
        name = request.POST['name']
        message_type = request.POST['message_type']
        contact = Contact(
            name=name,
            email=contact_email,
            company_name=company,
            contact_number=phone,
            message=message,
            message_type=message_type,
        )
        contact.save()

        email_context = {
            'company': company,
            'name': name,
            'phone': phone,
            'message': message,
            'email': contact_email,
        }

        subject = render_to_string(
            'contact_emails/contact_email_subject.txt',
            {'company': company}
        )
        body = render_to_string(
            'contact_emails/contact_email_body.txt', email_context

        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [to_email],
        )

        messages.success(request, "Your message was sent succesfully. You will hear from us soon.")
        return redirect(reverse('home'))

    template = 'contact.html'

    return render(request, template)
