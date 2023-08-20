from sms import send_sms

def send_sms_for_customer(message=None, number_to=None, number_from=None):
    send_sms(
        message,
        number_from,
        number_to,
        fail_silently=False
    )