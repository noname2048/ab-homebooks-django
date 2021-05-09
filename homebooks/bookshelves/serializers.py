from rest_framework.serializers import ModelSerializer

from bookshelves.models import Bookshelf
from accounts.serializers import UserSerializer


class BookshelfSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Bookshelf
        fields = ["user", "name"]
