import yaml
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand, CommandParser
from faker.factory import Factory
from yaml import dump

fake = Factory.create("en_US")
fake.seed(1)

User: AuthUser = get_user_model()


class Command(BaseCommand):
    help = "create some test users (debug mode only)"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            help="input is 20 when current user count is 10, make 10 more",
        )

        parser.add_argument("-p", "--prefix", type=str, help="username prefix.")

    def handle(self, *args, **options):
        if settings.DEBUG == False:
            print("this command only work on DEBUG MODE.")
            return 0

        try:
            cnt = options["cnt"]
        except:
            cnt = 5

        if not isinstance(cnt, int) or cnt < 1:
            print("user count must be positive integer")
            return 0

        created_number = 0
        created = []
        while created_number <= cnt:
            abstract_user = {
                "username": (username := fake.user_name()),
                "email": fake.email(),
                "password": make_password(username),
                "is_active": True,
            }
            print(abstract_user)
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(**abstract_user)
                created.append(abstract_user)
                created_number += 1

        print(f"{created_number} of users created")
        try:
            from yaml import CDumper as Dumper
        except ImportError:
            from yaml import Dumper
        with open("testusers.yaml", "a") as f:
            dump(created, f, Dumper)
