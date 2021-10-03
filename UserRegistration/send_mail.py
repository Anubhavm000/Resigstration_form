from django.core.mail import send_mail

def mail(receiver_mail,name):
    subject = "Registration for STACKFUSION"
    from_email = "STACKFUSION"
    to_email = [receiver_mail]
    mail_message = """Dear {},\nYOUR REGISTRATION ON STACKFUSION IS SUCCESSFULL!!""".format(name)

    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=mail_message, fail_silently=False)
