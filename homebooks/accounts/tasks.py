from celery import shared_task
from .models import User


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
