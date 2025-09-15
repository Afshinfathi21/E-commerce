from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender,instance,created,**kwargs):
    if created:
        message=f'Welcome {instance.username},Thanks for creating account.'
        print(message)
        # send_mail(
        #     subject='Welcome',
        #     from_email='myecommerce@site.com',
        #     message=message,
        #     recipient_list=[instance.email]
        # )