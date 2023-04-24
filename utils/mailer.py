from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from celery import shared_task


TEMPLATES = {
    'USER' : {
        'ACCOUNT' : {
            'LOCKED' : 'mails/account/locked.html',
            'RESET_PASSWORD_CONFIRMATION' : '',
        }
    },
}

SUBJECTS = {
    'USER' : {
        'ACCOUNT' : {
            'LOCKED' : 'Tu cuenta ha sido bloqueada.',
            'RESET_PASSWORD_CONFIRMATION' : '',
        }
    },
}

# Generic send email
@shared_task
def send_mail(subject,destination,content,template,reply_list=['noreply@example.com']):
    message = render_to_string(template, content)
    mail = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST,
        [destination],
        reply_to=reply_list
    )
    mail.content_subtype = "html"  
    mail.send()


def send_account_locked_email(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        user_profile = args[0]
        if user_profile.is_account_locked():
            send_mail.delay(
                SUBJECTS['USER']['ACCOUNT']['LOCKED'],
                user_profile.user.email,
                {'user': user_profile.user.email},
                TEMPLATES['USER']['ACCOUNT']['LOCKED']
            )
        return result

    return wrapper

