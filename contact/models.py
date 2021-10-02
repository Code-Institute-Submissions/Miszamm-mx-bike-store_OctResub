from django.db import models

# Create your models here.


class Contact(models.Model):
    ENQUIRY = 'EN'
    COMPLAIN = 'CM'
    MESSAGE_TYPE_CHOICES = [
        (ENQUIRY, 'Enquiry'),
        (COMPLAIN, 'Complain'),
    ]
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    company_name = models.CharField(max_length=100, blank=False, null=False)
    contact_number = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    message_type = models.CharField(
        max_length=2,
        choices=MESSAGE_TYPE_CHOICES,
        default=ENQUIRY
    )
