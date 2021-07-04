from celery import shared_task, app
from .models import User
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from homebooks import celery_app


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_user():
    return User.objects.count()


@shared_task
def user_isexist(email):
    user = User.objects.get(email=email)
    if user is not None:
        return True
    return False


@celery_app.task(serializer="json")
def send_welcome_mail(user: User):
    mail = Mail(
        from_email="sungwook.csw@noname2048.dev",
        to_emails=user.email,
        subject="welcome!",
        html_content="welcome email test",
    )
    sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
    response = sg.client.mail.send.post(request_body=mail.get())
    return response
