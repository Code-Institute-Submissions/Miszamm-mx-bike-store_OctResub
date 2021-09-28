from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

#  def contact(request):
#    """
#    This view handles the contact form
#    """
#
#    send_mail(
#        'Subject here',
#       'Here is the message.',
#        'miszamm@zohomail.eu',
#        ['miszamm@yahoo.ie'],
#        fail_silently=False,
#    )
#    return render(request, 'contact.html')


def contact(request):

    if request.POST:
        to_email = settings.DEFAULT_ORDER_EMAIL
        contact_email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        name = request.POST['name']

        email_context = {
            'name': name,
            'phone': phone,
            'message': message,
            'email': contact_email,
        }

        subject = render_to_string(
            'contact_emails/contact_email_subject.txt',
            {'name': name}
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

        messages.success(request, "Your message wassent succesfully. You will hear fromm us soon")
        return redirect(reverse('home'))

    template = 'contact.html'

    return render(request, template)
