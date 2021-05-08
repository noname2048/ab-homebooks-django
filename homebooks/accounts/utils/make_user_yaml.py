import yaml
from faker import Factory
from yaml import load, dump
from pathlib import Path

if not Path(Path(__file__).resolve() / "test_users.yaml").exists():

    fake = Factory.create("en_US")
    fake.seed(1)

    user_list = [{"username": fake.user_name(), "email": fake.email()} for _ in range(100)]

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper

    with open("test_users.yaml", "w") as f:
        dump(user_list, f)

else:
    with open("test_users.yaml", "w") as f:
        user_list = load(f, loader=yaml.FullLoader)

print(user_list)
