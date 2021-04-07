from django.dispatch import Signal, receiver

#Creating signals
notification = Signal(providing_args=['request', 'user'])


# Receiver Function
@receiver(notification)
def shpw_notification(sender, **kwargs):
    print(sender)
    print(f'Kwargs: {kwargs}')
    print('Notification')
